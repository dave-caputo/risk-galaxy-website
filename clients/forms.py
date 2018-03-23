from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field

from django import forms

from clients.models import Client


class ClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set up crispy forms...
        self.helper = FormHelper()
        self.helper.form_id = 'demo_request_form'
        self.helper.layout = Layout(
            'name',
            'email',
            'country',
            PrependedText('phone', '...'),
            Field('phone_code', type='hidden'),
            'org',
            'org_url'
        )

        # Set mandatory fields...
        for i in ['name', 'email', 'country', 'phone', 'phone_code', 'org']:
            self.fields[i].required = True

    class Meta:
        fields = [
            'name', 'email', 'country', 'phone', 'phone_code', 'org',
            'org_url']

        model = Client
