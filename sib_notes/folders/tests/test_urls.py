import pytest
from django.urls import resolve, reverse

from .factories import FolderFactory


@pytest.fixture
def folder():
    return FolderFactory()


pytestmark = pytest.mark.django_db


def test_folder_reverse():
    """
    Tests if list view is redirected to the right URL
    :return:
    """
    assert reverse("folders:list") == "/folders/"


def test_folder_list_resolve():
    """
    Tests if /folders/ URL resolves to the right view
    :return:
    """
    assert resolve("/folders/").view_name == "folders:list"


def test_add_folder_reverse():
    """
    Tests if add folder view is directed to the right URL
    :return:
    """
    assert reverse("folders:add") == "/folders/add/"


def test_add_folder_resolve():
    """
    Tests if /folders/add URL resolves to the right view
    :return:
    """
    assert resolve("/folders/add/").view_name == "folders:add"


def test_update_folder_reverse(folder):
    """
    Tests if update folder view is directed to the right URL
    :param folder:
    :return:
    """
    url = reverse("folders:update", kwargs={"slug": folder.slug})
    assert url == f"/folders/{folder.slug}/update/"


def test_update_folder_resolve(folder):
    """
    Tests if /folders/{folder.slug}/update resolves to the right view
    :param folder:
    :return:
    """
    assert resolve(f"/folders/{folder.slug}/update/").view_name == "folders:update"


def test_folder_detail_reverse(folder):
    """
    Tests if folder detail view is directed to the right URL
    :param folder:
    :return:
    """
    url = reverse("folders:detail", kwargs={"slug": folder.slug})
    assert url == f"/folders/{folder.slug}/"


def test_folder_detail_resolve(folder):
    """
    Tests if /folders/{folder.slug}/ resolves to the right view
    :param folder:
    :return:
    """
    url = f"/folders/{folder.slug}/"
    assert resolve(url).view_name == "folders:detail"
