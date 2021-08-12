from django.urls import path

from . import views

app_name = "folders"
urlpatterns = [
    path("", view=views.FolderListView.as_view(), name="list"),
    path(route="add/", view=views.FolderCreateView.as_view(), name="add"),
    path(route="<slug:slug>/", view=views.FolderDetailView.as_view(), name="detail"),
    path(
        route="<slug:slug>/update/",
        view=views.FolderUpdateView.as_view(),
        name="update",
    ),
]
