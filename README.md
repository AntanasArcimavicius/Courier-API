# Courier-API
Django application with API endpoints for courier working time management.
API endpoints:
  CRUD views for working time management.
    Validation rules for create/update:
      - End time should not come before start time.
      - There should be no overlapping working times per courier.
Gets a number of active couriers for each time range from CSV
