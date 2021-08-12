import pytest
from django.urls import resolve, reverse

from .factories import FolderFactory


@pytest.fixture
def folder():
    return FolderFactory()


pytestmark = pytest.mark.django_db


def test_folder_reverse():
    assert reverse("folders:list") == "/folders/"


def test_folder_list_resolve():
    assert resolve("/folders/").view_name == "folders:list"


def test_add_folder_reverse():
    assert reverse("folders:add") == "/folders/add/"


def test_add_folder_resolve():
    assert resolve("/folders/add/").view_name == "folders:add"


def test_update_folder_reverse(folder):
    url = reverse("folders:update", kwargs={"slug": folder.slug})
    assert url == f"/folders/{folder.slug}/update/"


def test_update_folder_resolve(folder):
    assert resolve(f"/folders/{folder.slug}/update/").view_name == "folders:update"


def test_folder_detail_reverse(folder):
    url = reverse("folders:detail", kwargs={"slug": folder.slug})
    assert url == f"/folders/{folder.slug}/"


def test_folder_detail_resolve(folder):
    url = f"/folders/{folder.slug}/"
    assert resolve(url).view_name == "folders:detail"
