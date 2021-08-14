import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from sib_notes.users.tests.factories import UserFactory

from ..models import Folder
from .factories import FolderFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def folder():
    return FolderFactory()


pytestmark = pytest.mark.django_db


def test_good_folder_list_view(client, user):
    """
    Tests if /folders/ returns the correct view
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)
    response = client.get(reverse("folders:list"))
    assertContains(response, "Folder List")


def test_good_folder_detail_view(client, user, folder):
    """
    Tests if /folders/{folder.slug}/ returns the correct view
    :param client:
    :param user:
    :param folder: A Folder object created by the FolderFactory fixture
    :return:
    """
    client.force_login(user)
    response = client.get(reverse("folders:detail", kwargs={"slug": folder.slug}))
    assertContains(response, folder.name)


def test_good_folder_create(client, user):
    """
    Tests if /folders/add/ return the correct view
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)
    url = reverse("folders:add")
    response = client.get(url)
    assert response.status_code == 200


def test_folder_list_contains_2_folders(client, user):
    """
    Creates two Folder objects and tests if both are listed
    in /folders/
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)

    folder1 = FolderFactory()
    folder2 = FolderFactory()

    response = client.get(reverse("folders:list"))

    assertContains(response, folder1.name)
    assertContains(response, folder2.name)


def test_folder_detail_view_contains_folder_data(client, user, folder):
    """
    Tests if FolderDetailView displays the correct folder object
    :param client:
    :param user:
    :param folder: A Folder object created by the FolderFactory fixture
    :return:
    """
    client.force_login(user)

    response = client.get(reverse("folders:detail", kwargs={"slug": folder.slug}))

    assertContains(response, folder.name)
    assertContains(response, folder.creator)


def test_folder_create_form_valid(client, user):
    """
    Tests creating a folder with valid input
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)

    url = reverse("folders:add")
    form_data = {"name": "Test Folder"}
    response = client.post(url, form_data)

    assert response.status_code == 302

    new_folder = Folder.objects.get(name="Test Folder")

    assert new_folder.creator == user


def test_folder_create_correct_title(client, user):
    """
    Tests if requesting the FolderCreateView returns the correct template,
    as FolderCreateView and FolderCreateView use the same template file
    :param client:
    :param user:
    :return:
    """
    client.force_login(user)
    url = reverse("folders:add")
    response = client.get(url)
    assertContains(response, "Add Folder")


def test_good_folder_update_view(client, user, folder):
    """
    Tests if requesting the NoteUpdateView returns the correct template,
    as FolderCreateView and FolderCreateView use the same template file
    :param client:
    :param user:
    :param folder: A Folder object created by the FolderFactory fixture
    :return:
    """
    client.force_login(user)
    url = reverse("folders:update", kwargs={"slug": folder.slug})
    response = client.get(url)
    assertContains(response, "Update Folder")


def test_folder_update(client, user, folder):
    """
    Tests updating a folder given valid input
    :param client:
    :param user:
    :param folder: A Folder object created by the FolderFactory fixture
    :return:
    """
    client.force_login(user)
    url = reverse("folders:update", kwargs={"slug": folder.slug})
    form_data = {
        "name": "New Folder",
    }
    client.post(url, form_data)
    folder.refresh_from_db()
    assert folder.name == "New Folder"
