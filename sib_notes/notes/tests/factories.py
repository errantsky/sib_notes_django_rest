import factory
import factory.fuzzy
import pytest
from django.template.defaultfilters import slugify

from sib_notes.users.tests.factories import UserFactory

from ..models import Note


@pytest.fixture
def note():
    return NoteFactory()


class NoteFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    text = factory.Faker(
        "paragraph",
        nb_sentences=3,
        variable_nb_sentences=True,
    )
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Note
