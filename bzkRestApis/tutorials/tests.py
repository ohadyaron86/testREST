from django.test import TestCase
from rest_framework.test import APIClient
from tutorials.models import Tutorial


class TestModel(TestCase):
    def setUp(self):
        Tutorial.objects.create(
            title='T1', description='T1 description', published=True)
        Tutorial.objects.create(
            title='T2', description='T2 description', published=True)

    def test_something_that_will_pass(self):
        t1 = Tutorial.objects.get(title='T1')
        t2 = Tutorial.objects.get(title='T2')
        self.assertEqual(
            t1.description, "T1 description")
        self.assertEqual(
            t2.description, "T2 description")

    def test_something_that_will_fail(self):
        t1 = Tutorial.objects.get(title='T1')
        self.assertNotEqual(
            t1.description, "T2 description")

    def tearDown(self):
        # Clean up run after every test method.
        pass


class TestView(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        client = APIClient()
        # client.post('/notes/', {'title': 'new idea'}, format='json')
        response = client.get('/api/tutorials/8')
        # response = self.client.get()
        self.assertEqual(response.status_code, 200)
