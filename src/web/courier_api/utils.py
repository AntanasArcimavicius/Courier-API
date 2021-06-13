import csv, json, io
from rest_framework import serializers

from .models import Courier


def check_if_time_is_valid(serializer):
    '''
    Checks for custom Validation rules
    '''
    start_time = serializer.validated_data['start_time']
    end_time = serializer.validated_data['end_time']
    courier_list = Courier.objects.all()

    if start_time >= end_time:
        raise serializers.ValidationError(('End time should not come before start time'))

    for courier in courier_list:
        if start_time < courier.end_time and start_time >= courier.start_time:
            raise serializers.ValidationError(('Start time is in others period range'))
        if end_time <= courier.end_time and end_time > courier.start_time:
            raise serializers.ValidationError(('Start time is in others period range'))


def couriers_list_from_csv(serializer):
    '''
    makes list of couriers from csv
    '''
    courier_list = []

    courier_data = serializer.validated_data['courier_list']
    decoded_file = courier_data.read().decode()
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string)

    for row in reader:
        courier_list.append({
            'name': row[0],
            'start_time': row[1],
            'end_time': row[2],
        })

    return courier_list


def get_active_couriers(courier_list):
    '''
    sorts time, removes time duplicates, checks if courier is active in time range
    and creates a list for periods
    '''
    time_list = []
    active_courier_list = []

    for courier in courier_list:
        time_list.append(courier['start_time'])
        time_list.append(courier['end_time'])

    sorted_time = sorted(list(dict.fromkeys(time_list)))

    for index, time in enumerate(sorted_time[0:len(sorted_time)-1]):
        active_names_list = []
        period_start = time
        period_end = sorted_time[index+1]

        for courier in courier_list:

            if courier['start_time'] <= period_start and courier['end_time'] >= period_end:
                active_names_list.append(courier['name'])

        active_number = len(active_names_list)

        active_courier_list.append({
            'period_start_time': period_start,
            'period_end_time': period_end,
            'number_of_active_couriers': active_number,
            'active_courier_names': active_names_list,
        })

    return active_courier_list


def active_couriers_json(serializer):
    '''
    dumps json into view for response
    '''
    courier_list = couriers_list_from_csv(serializer)
    active_couriers = get_active_couriers(courier_list)

    return json.dumps(active_couriers)


