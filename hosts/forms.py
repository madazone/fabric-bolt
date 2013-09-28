from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

import models


class HostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Host

    helper = FormHelper()
    helper.layout = Layout(
        'name',
        ButtonHolder(
            Submit('submit', 'Create Host', css_class='button')
        )
    )


class HostUpdateForm(HostCreateForm):

    helper = FormHelper()
    helper.layout = Layout(
        'name',
        ButtonHolder(
            Submit('submit', 'Update Host', css_class='button')
        )
    )