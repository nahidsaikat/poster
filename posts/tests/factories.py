import factory
from faker import Faker
from faker.providers import internet, lorem, person, python, phone_number

from posts.models import Post


fake = Faker()
fake.add_provider(internet)
fake.add_provider(lorem)
fake.add_provider(person)
fake.add_provider(python)
fake.add_provider(phone_number)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=10))
    caption = factory.LazyAttribute(lambda _: fake.sentence(nb_words=30))
