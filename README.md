# Courier-API
Django application with API endpoints for courier working time management.
API endpoints:
  CRUD views for working time management.
    Validation rules for create/update:
      - End time should not come before start time.
      - Make sure there are no overlapping working times per courier.
Get a number of active couriers for each time range.
