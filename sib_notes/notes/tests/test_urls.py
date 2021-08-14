import pytest
from django.urls import resolve, reverse

from .factories import NoteFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def note():
    return NoteFactory()


def test_note_reverse():
    """
    Tests if list view is directed to the right URL
    :return:
    """
    assert reverse("notes:list") == "/notes/"


def test_list_resolve():
    """
    Tests if /notes/ URL resolves to the right view
    :return:
    """
    assert resolve("/notes/").view_name == "notes:list"


def test_add_reverse():
    """
    Tests if note add view is directed to the right URL
    :return:
    """
    assert reverse("notes:add") == "/notes/add/"


def test_add_resolve():
    """
    Tests if /notes/add URL resolves to the right view
    :return:
    """
    assert resolve("/notes/add/").view_name == "notes:add"


def test_detail_reverse(note):
    """
    Tests if note detail view is directed to the right URL
    :param note:
    :return:
    """
    url = reverse("notes:detail", kwargs={"slug": note.slug})
    assert url == f"/notes/{note.slug}/"


def test_detail_resolve(note):
    """
    Tests if /notes/{note.slug}/ URL resolves to the right view
    :param note:
    :return:
    """
    url = f"/notes/{note.slug}/"
    assert resolve(url).view_name == "notes:detail"
