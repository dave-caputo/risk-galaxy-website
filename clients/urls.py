from django.urls import path
from clients import views

app_name = 'clients'

urlpatterns = [
    path(
        'demo-request-create/',
        views.ClientDemoRequestCreateView.as_view(),
        name='demo_request_form'),

    path(
        'demo-request-success/',
        views.ClientDemoRequestSuccessView.as_view(),
        name='demo_request_success')
]
