import pytest

from .factories import NoteFactory

pytestmark = pytest.mark.django_db

# TODO add test comments


def test__str__():
    """
    Tests if Note's __str__ method returns the correct string
    :return:
    """
    note = NoteFactory()
    assert note.title == note.__str__()
    assert note.title == str(note)


def test_get_absolute_url():
    """
    Tests if Note's get_absolute_url() returns the correct URL
    :return:
    """
    note = NoteFactory()
    assert note.get_absolute_url() == f"/notes/{note.slug}/"
