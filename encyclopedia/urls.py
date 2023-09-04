from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.show_entry, name="show_entry"),
    path("wiki/search/", views.search_entry, name="search_entry"), 
    path("new/", views.new_entry, name="new_entry"),
    path("edit/", views.edit_entry, name="edit_entry"), 
    path("save/", views.save_entry, name="save_entry"), 
    path("random/", views.random_entry, name="random_entry")
]
