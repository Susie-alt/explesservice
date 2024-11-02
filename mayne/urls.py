from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/check_delivery/", views.check_delivery, name="check_delivery"),
    path("", views.home, name="home"),
    path("under_construction/", views.under_construction, name="under_construction"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("<int:id>/edit/", views.edit, name="edit"),
    path("<int:id>/delete/", views.delete_delivery, name="delete"),
    path("<int:id>/get_updates/", views.get_updates, name="get_updates"),
    path("pot_covers/", views.pot_covers, name="pot_covers"),
]