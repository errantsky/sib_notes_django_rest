import pytest

from .factories import FolderFactory


@pytest.fixture
def folder():
    return FolderFactory()


pytestmark = pytest.mark.django_db


def test__str__(folder):
    assert folder.__str__() == folder.name
    assert str(folder) == folder.name


def test_get_absolute_url(folder):
    assert folder.get_absolute_url() == f"/folders/{folder.slug}/"
