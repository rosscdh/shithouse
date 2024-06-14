from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from shithouse.apps.house import models
from shithouse.apps.house import forms

class HouseListView(ListView):
    model = models.Address


class HouseDetailView(DetailView):
    model = models.Address


class HouseFormView(CreateView):
    form_class = forms.AddressForm
    template_name = "house/address_form.html"

    def get_success_url(self) -> str:
        return reverse_lazy("house-detail", kwargs=dict(pk=self.object.pk))