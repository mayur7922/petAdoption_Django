from django.urls import path #type: ignore
from django.contrib import admin #type: ignore
from . import views

urlpatterns = [
    path(
        "admin/pets/<int:id>",
        views.PetRetrieveUpdateDestory.as_view(),
        name="Update and Delete",
    ),
    path("admin/pets/", views.PetListCreate.as_view(), name="pet-view-create"),
    path('', views.RunningView.as_view(), name='running'),
    path('admin/', admin.site.urls)
]
