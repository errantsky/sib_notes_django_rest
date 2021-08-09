import pytest

from .factories import NoteFactory

pytestmark = pytest.mark.django_db


def test__str__():
    note = NoteFactory()
    assert note.title == note.__str__()
    assert note.title == str(note)


def test_get_absolute_url():
    note = NoteFactory()
    assert note.get_absolute_url() == f"/notes/{note.slug}/"
