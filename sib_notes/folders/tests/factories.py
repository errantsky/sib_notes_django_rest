import factory
import factory.fuzzy
import pytest
from django.template.defaultfilters import slugify

from sib_notes.users.tests.factories import UserFactory

from ..models import Folder


@pytest.fixture
def folder():
    return FolderFactory()


class FolderFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Folder
