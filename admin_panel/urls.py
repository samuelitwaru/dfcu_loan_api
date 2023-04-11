from django.urls import path

from .views import *

app_name = "admin_panel"


urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('docs', docs, name='docs'),

]
