from typing import Any
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Address


class AddressForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Address
        fields = (
            "address",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'house-create'
        self.helper.add_input(Submit('submit', 'Submit', css_class="is-success"))

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if Address.objects.filter(address=address).count() > 0:
            raise forms.ValidationError(
                "Address already exists: %(value)s",
                params={"value": address},
            )
        return address

    def save(self, commit: bool = True) -> Any:
        # append misc fields into data object
        for key, field in self.fields.items():
            if key not in self.Meta.fields:
                self.instance.data[key] = self.cleaned_data.get(key)
        return super().save(commit)