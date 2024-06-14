from django.urls import path

from shithouse.apps.house import views

urlpatterns = [
    path("address/", views.HouseListView.as_view(), name="house"),
    path("address/create", views.HouseFormView.as_view(), name="house-create"),
    path("address/<int:pk>/", views.HouseDetailView.as_view(), name="house-detail"),
]