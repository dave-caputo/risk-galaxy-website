from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from clients.forms import ClientForm
from clients.models import Client


class ClientDemoRequestCreateView(CreateView):
    form_class = ClientForm
    model = Client
    template_name = 'clients/demo_request_form.html'
    success_url = reverse_lazy('clients:demo_request_success')


class ClientDemoRequestSuccessView(TemplateView):
    template_name = 'clients/demo_request_success.html'
