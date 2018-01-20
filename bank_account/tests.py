from bank_account.models import BankAccountUser

from django.test import TestCase


class UserTest(TestCase):

    # def setUp(self):
    #     self.user = User.objects.create_user(username='test1', password='test')
    #     self.user.save()

    # def user_login(self):
    #     self.client.login(username='test1', password='test')

    def setUp(self):
        admin = BankAccountUser(username='admin')
        admin.set_password("testpassword")
        admin.is_admin = True
        admin.save()
        self.adminuser = admin
        user = BankAccountUser(username='user')
        user.set_password("testpassword")
        user.is_admin = False
        user.creator = admin
        user.save()
        self.user = user

    def test_list_users_no_logging(self):
        action = self.client.get("/users/list/")
        self.assertEqual(action.status_code, 302)

    def test_list_users_logging(self):
        self.client.login(username='admin', password='testpassword')
        action = self.client.get("/users/list/")
        self.assertEqual(action.status_code, 200)

    def test_add_user_no_logging(self):
        action = self.client.get("/users/add/")
        self.assertEqual(action.status_code, 302)

    def test_add_user_logging(self):
        action = self.client.post('/users/add/', {
            'username': 'testuser',
            'first_name': 'test',
            'last_name': 'user',
            'password': 'password',
            'iban': 'CH5982876111158263574',
        })
        self.assertEqual(action.status_code, 302)
