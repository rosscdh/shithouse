from django.urls import path

from shithouse.apps.agency import views

urlpatterns = [
    path("agency/", views.AgencyListView.as_view(), name="agency"),
    path("agency/create", views.AgencyFormView.as_view(), name="agency-create"),
    path("agency/<int:pk>/", views.AgencyDetailView.as_view(), name="agency-detail"),
    path("agency/<int:agency_pk>/branch/", views.AgencyBranchListView.as_view(), name="branch"),
    path("agency/<int:agency_pk>/branch/create", views.BranchFormView.as_view(), name="branch-create"),
    path("agency/<int:agency_pk>/branch/<int:pk>/", views.AgencyBranchDetailView.as_view(), name="branch-detail"),
    path("agent/", views.AgentListView.as_view(), name="agent"),
    path("agent/create", views.AgentFormView.as_view(), name="agent-create"),
    path("agent/<int:pk>/", views.AgentDetailView.as_view(), name="agent-detail"),
]