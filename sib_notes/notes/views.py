from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note

    fields = [
        "title",
        "text",
        "parent_folder",
    ]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note

    fields = [
        "title",
        "text",
        "parent_folder",
    ]

    action = "Update"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    # get_context_data
