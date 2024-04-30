from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Course, Lesson, Subscribe
from users.models import User


# Data for create lesson
data_create = {
    'name': 'Урок для тестирования 1',
    'description': 'Описание урока для тестирования 1',
    'link_video': 'https://www.youtube.com/test1',
    'owner': 1,
    'course': 1
}
# Data for control test create lesson
data_create_control = {
    "id": 2,
    "name": "Урок для тестирования 1",
    "preview": None,
    "description": "Описание урока для тестирования 1",
    "link_video": 'https://www.youtube.com/test1',
    "owner": 1,
    "course": [
        1
    ]
}
# Data for update lesson
data_update = {
    'name': 'Урок для тестирования 2',
    'description': 'Описание урока для тестирования 2',
    'link_video': 'https://www.youtube.com/test2'
}


class LessonModelTest(APITestCase):
    """
    Test CRUD views for Lesson model.
    """

    def setUp(self):
        # Create user and authorize for testing
        self.user = User.objects.create(
            email='test@test.ov'
        )
        self.user.set_password('123qwe456rty')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        # Create course for testing
        self.course = Course.objects.create(
            name='Курс для тестирования',
            description='Описание курса для тестирования',
            owner=self.user
        )

        # Create lesson for testing
        self.lesson = Lesson.objects.create(
            name='Урок для тестирования',
            description='Описание урока для тестирования',
            link_video='https://www.youtube.com/test',
            owner=self.user,
        )
        # Set course for last lesson
        Lesson.objects.last().course.set([self.course.id])

    def test_create_lesson(self):
        """Test create lesson."""
        url_create = reverse('lms:lesson-create')
        response = self.client.post(url_create, data=data_create)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check existence object
        self.assertTrue(Lesson.objects.filter(name=data_create['name']).exists())
        # Check data
        self.assertEqual(response.json(), data_create_control)

    def test_retrieve_lesson(self):
        """Test read lesson."""
        url_retrieve = reverse('lms:lesson-get', args=[self.lesson.id])
        response = self.client.get(url_retrieve)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data
        self.assertEqual(response.data['name'], self.lesson.name)

    def test_list_lesson(self):
        """Test list lesson."""
        url_list = reverse('lms:lesson-list')
        response = self.client.get(url_list)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check length list
        self.assertEqual(len(response.data), 4)

    def test_update_lesson(self):
        """Test update lesson."""
        url_update = reverse('lms:lesson-update', args=[self.lesson.id])
        response = self.client.patch(url_update, data=data_update)

        # Data for control test for update lesson
        data_update_control = {
            "id": self.lesson.id,
            "name": "Урок для тестирования 2",
            "preview": None,
            "description": "Описание урока для тестирования 2",
            "link_video": 'https://www.youtube.com/test2',
            "owner": self.user.id,
            "course": [
                self.course.id
            ]
        }

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data
        self.assertEqual(response.json(), data_update_control)

    def test_delete_lesson(self):
        """Test delete lesson."""
        url_delete = reverse('lms:lesson-delete', args=[self.lesson.id])
        response = self.client.delete(url_delete)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscribeModelTest(APITestCase):
    """Test add and destroy view for Subscribe model."""

    def setUp(self):
        # Create user and authorize for testing
        self.user = User.objects.create(
            email='test2@test.ov'
        )
        self.user.set_password('123qwe456rty')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        # Create course for testing
        self.course = Course.objects.create(
            name='Курс для тестирования3',
            description='Описание курса для тестирования3',
            owner=self.user
        )

    def test_add_subscribe(self):
        """Test add subscribe."""
        url = reverse('lms:subscribe-post')

        # Data for testing
        data = {
            'user': self.user.id,
            'course': self.course.id
        }

        response = self.client.post(url, data=data)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check existence object
        self.assertTrue(Subscribe.objects.filter(user=self.user, course=self.course).exists())

    def test_delete_subscribe(self):
        """Test delete subscribe."""
        url = reverse('lms:subscribe-post')
        data = {
            'user': self.user.id,
            'course': self.course.id
        }
        response = self.client.post(url, data=data)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
