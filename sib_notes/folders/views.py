from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Folder


# Create your views here.
class FolderDetailView(LoginRequiredMixin, DetailView):
    model = Folder


class FolderListView(LoginRequiredMixin, ListView):
    model = Folder


class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder

    fields = [
        "name",
    ]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)


class FolderUpdateView(LoginRequiredMixin, UpdateView):
    model = Folder

    fields = [
        "name",
    ]

    action = "Update"
