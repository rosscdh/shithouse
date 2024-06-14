from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from shithouse.apps.agency import models

from shithouse.apps.agency import forms


class AgencyListView(ListView):
    model = models.Agency


class AgencyDetailView(DetailView):
    model = models.Agency


class AgencyBranchListView(ListView):
    model = models.Branch


class AgencyBranchDetailView(DetailView):
    model = models.Branch


class AgentListView(ListView):
    model = models.Agent


class AgentDetailView(DetailView):
    model = models.Agent


class AgencyFormView(CreateView):
    form_class = forms.AgencyForm
    template_name = "agency/agency_form.html"

    def get_success_url(self) -> str:
        return reverse_lazy("agency-detail", kwargs=dict(pk=self.object.pk))


class BranchFormView(CreateView):
    form_class = forms.AgencyForm
    template_name = "agency/branch_form.html"

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data.update(dict(
            agency=models.Agency.objects.get(pk=self.kwargs.get("agency_pk"))
        ))
        return data

    def get_success_url(self) -> str:
        return reverse_lazy("branch-detail", kwargs=dict(pk=self.object.pk))


class AgentFormView(CreateView):
    form_class = forms.AgentForm
    template_name = "agency/agent_form.html"

    def get_success_url(self) -> str:
        return reverse_lazy("agent-detail", kwargs=dict(pk=self.object.pk))