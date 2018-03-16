from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper, Layout

from django import forms

from clients.models import Client


class ClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set up crispy forms...
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'country',
            PrependedText('phone', '+1'),
            'org',
            'org_url'
        )
        self.helper.form_id = 'demo_request_form'

        # Set mandatory fields...
        for i in ['name', 'email', 'country', 'phone', 'org']:
            self.fields[i].required = True

    class Meta:
        fields = ['name', 'email', 'country', 'phone', 'org', 'org_url']
        model = Client
