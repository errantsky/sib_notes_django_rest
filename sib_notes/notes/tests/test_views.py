import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from ...folders.tests.factories import FolderFactory
from ..models import Note
from .factories import NoteFactory, UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def note():
    return NoteFactory()


@pytest.fixture
def folder():
    return FolderFactory()


pytestmark = pytest.mark.django_db


def test_good_notes_list_view(client, user):
    """
    Tests if /notes/ returns the correct view
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)
    response = client.get(reverse("notes:list"))
    assertContains(response, "Note List")


def test_good_note_detail_view(client, user, note):
    """
    Tests if /notes/{note.slug}/ returns the correct view
    :param client:
    :param user:
    :param note: A note object created by the NoteFactory fixture
    :return:
    """
    client.force_login(user)
    url = reverse("notes:detail", kwargs={"slug": note.slug})
    response = client.get(url)
    assertContains(response, note.title)


def test_good_note_create_view(client, user):
    """
    Tests if /notes/add returns the correct view
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)
    url = reverse("notes:add")
    response = client.get(url)
    assert response.status_code == 200


def test_note_list_contains_2_notes(client, user):
    """
    Creates two note objects and tests if both are listed
    in /notes/
    :param client:
    :param user:
    :return:
    """
    note1 = NoteFactory()
    note2 = NoteFactory()

    client.force_login(user)
    response = client.get(reverse("notes:list"))

    assertContains(response, note1.title)
    assertContains(response, note2.title)


def test_note_detail_contains_note_data(client, user, note):
    """
    Tests if NoteDetailView displays the correct Note object
    :param client:
    :param user:
    :param note:
    :return:
    """
    client.force_login(user)

    response = client.get(reverse("notes:detail", kwargs={"slug": note.slug}))

    assertContains(response, note.title)
    assertContains(response, note.text)
    assertContains(response, note.creator)


def test_note_create_form_valid(client, user, folder):
    """
    Tests creating a note with valid input
    :param client:
    :param user:
    :param folder: A Folder object created by the FolderFactory fixture
    :return:
    """
    client.force_login(user)
    form_data = {
        "title": "Test Note",
        "text": "Here's a note for testing.",
        "parent_folder": folder.id,
    }
    url = reverse("notes:add")
    response = client.post(url, form_data)

    assert response.status_code == 302

    note = Note.objects.get(title="Test Note")

    assert note.text == form_data["text"]
    assert note.creator == user
    assert note.parent_folder == folder


def test_note_create_correct_title(client, user):
    """
    Tests if requesting the NoteCreateView returns the correct template,
    as NoteCreateView and NoteCreateView use the same template file
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)
    url = reverse("notes:add")
    response = client.get(url)
    assertContains(response, "Add Note")


def test_good_note_update_view(client, user, note):
    """
    Tests if requesting the NoteUpdateView returns the correct template,
    as NoteCreateView and NoteCreateView use the same template file
    :param client:
    :param user:
    :param note: A Note object created by the NoteFactory fixture
    :return:
    """
    client.force_login(user)
    url = reverse("notes:update", kwargs={"slug": note.slug})
    response = client.get(url)
    assertContains(response, "Update Note")


def test_note_update(client, user, note, folder):
    """
    Tests updating a note given valid input
    :param client:
    :param user:
    :param note: A Note object created by the NoteFactory fixture
    :param folder: A Folder object created by the FolderFactory fixture
    :return:
    """
    client.force_login(user)

    url = reverse("notes:update", kwargs={"slug": note.slug})
    form_data = {
        "title": note.title,
        "text": "something new",
        "parent_folder": folder.id,
    }
    response = client.post(url, form_data)

    assert response.status_code == 302

    note.refresh_from_db()
    assert note.text == "something new"
    assert note.parent_folder == folder
