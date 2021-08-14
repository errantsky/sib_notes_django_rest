import pytest

from .factories import FolderFactory


@pytest.fixture
def folder():
    return FolderFactory()


pytestmark = pytest.mark.django_db


def test__str__(folder):
    """
    Tests if Folder's __str__ method return the correct string
    :param folder:
    :return:
    """
    assert folder.__str__() == folder.name
    assert str(folder) == folder.name


def test_get_absolute_url(folder):
    """
    Tests if Folder's get_absolute_url returns the correct URL
    :param folder:
    :return:
    """
    assert folder.get_absolute_url() == f"/folders/{folder.slug}/"
