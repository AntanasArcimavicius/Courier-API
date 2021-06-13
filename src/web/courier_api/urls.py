from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import CourierView

app_name = 'courier_api'

router = DefaultRouter()
router.register('', CourierView, basename='courier_api')
urlpatterns = router.urls