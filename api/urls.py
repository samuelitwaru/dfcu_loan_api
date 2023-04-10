from django.urls import path

from .views import *

# from core.views.other import read_nationalities
# from wex import router


# app_name = "core"

# router.register(r'entities', EntityViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'items', ItemViewSet)
# router.register(r'metric-systems', MetricSystemViewSet)
# router.register(r'metrics', MetricViewSet)

urlpatterns = [
    path('', loan_status, name='loan_status'),
    path('download-response', download_response, name='download_response'),
]