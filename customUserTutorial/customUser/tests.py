from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class UsersManagersTests(TestCase):

    def test_create_user(self):
        _user = get_user_model()
        user = _user.objects.create_user(email='test@user.com', password='test0123!')
        self.assertEqual(user.email, 'test@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            _user.objects.create_user()
        with self.assertRaises(TypeError):
            _user.objects.create_user(email='')
        with self.assertRaises(ValueError):
            _user.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        _user = get_user_model()
        admin_user = _user.objects.create_superuser('test@super.com', 'test0123!')
        self.assertEqual(admin_user.email, 'test@super.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            _user.objects.create_superuser(email='test@super.com', password='test0123!', is_superuser=False)
