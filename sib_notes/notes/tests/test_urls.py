import pytest
from django.urls import resolve, reverse

from .factories import NoteFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def note():
    return NoteFactory()


def test_note_reverse():
    assert reverse("notes:list") == "/notes/"


def test_list_resolve():
    assert resolve("/notes/").view_name == "notes:list"


def test_add_reverse():
    assert reverse("notes:add") == "/notes/add/"


def test_add_resolve():
    assert resolve("/notes/add/").view_name == "notes:add"


def test_detail_reverse(note):
    url = reverse("notes:detail", kwargs={"slug": note.slug})
    assert url == f"/notes/{note.slug}/"


def test_detail_resolve(note):
    url = f"/notes/{note.slug}/"
    assert resolve(url).view_name == "notes:detail"
