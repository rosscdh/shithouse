from typing import Any
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Agency, Agent, Branch

class FormDataToJsonDataFieldMixin:
    def save(self, commit: bool = True) -> Any:
        # append misc fields into data object
        for key, field in self.fields.items():
            if key not in self.Meta.fields:
                self.instance.data[key] = self.cleaned_data.get(key)
        return super().save(commit)


class AgencyForm(FormDataToJsonDataFieldMixin, forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Agency
        fields = (
            "name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'agency-create'
        self.helper.add_input(Submit('submit', 'Submit', css_class="is-success"))

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if Agency.objects.filter(address=address).count() > 0:
            raise forms.ValidationError(
                "Agency already exists: %(value)s",
                params={"value": address},
            )
        return address


class BranchForm(FormDataToJsonDataFieldMixin, forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Agency
        fields = (
            "name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'branch-create'
        self.helper.add_input(Submit('submit', 'Submit', css_class="is-success"))

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if Branch.objects.filter(address=address).count() > 0:
            raise forms.ValidationError(
                "Branch already exists: %(value)s",
                params={"value": address},
            )
        return address


class AgentForm(FormDataToJsonDataFieldMixin, forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    branches = forms.ModelMultipleChoiceField(queryset=Branch.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Agent
        fields = (
            "name", "branches",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'agent-create'
        self.helper.add_input(Submit('submit', 'Submit', css_class="is-success"))

