import io

from django.urls import reverse
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase
from PIL import Image
from faker import Faker
from faker.providers import internet, lorem, person

from .factories import PostFactory

fake = Faker()
fake.add_provider(internet)
fake.add_provider(lorem)
fake.add_provider(person)


class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.PostModel = PostFactory._meta.model

    def test_create_post_success(self):
        data = {
            'title': fake.sentence(nb_words=10),
            'caption': fake.sentence(nb_words=30)
        }
        response = self.client.post(reverse('posts-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], data['title'])
        self.assertEqual(response.json()['caption'], data['caption'])

    def test_create_post_title_missing(self):
        data = {
            'caption': fake.sentence(nb_words=30)
        }
        response = self.client.post(reverse('posts-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_post_success(self):
        post = PostFactory.create()
        data = {
            'title': 'title',
            'caption': 'caption'
        }
        response = self.client.patch(reverse('posts-detail', args=[post.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], data['title'])
        self.assertEqual(response.json()['caption'], data['caption'])

        db_instance = self.PostModel.objects.get(id=post.id)
        self.assertEqual(db_instance.title, data['title'])
        self.assertEqual(db_instance.caption, data['caption'])

    def test_update_post_title_missing(self):
        post = PostFactory.create()
        data = {
            'caption': 'caption'
        }
        response = self.client.put(reverse('posts-detail', args=[post.id]), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PostFileAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = PostFactory.create()

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    @override_settings(
        MEDIA_ROOT='test_file'
    )
    def test_post_file_upload(self):
        photo_file = self.generate_photo_file()

        data = {
            'file': photo_file
        }
        url = reverse('post-file-upload', args=[self.post.id])
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['post'], self.post.id)
