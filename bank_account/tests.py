from bank_account.models import BankAccountUser

from django.test import TestCase


class UserTest(TestCase):

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
        notcreator = BankAccountUser(username='notCreator')
        notcreator.set_password("testpassword")
        notcreator.is_admin = True
        notcreator.save()
        self.notcreator = notcreator

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

    def test_user_profile_no_logging(self):
        action = self.client.get("/users/" + str(self.user.id) + "/")
        self.assertEqual(action.status_code, 302)

    def test_user_profile_logging(self):
        self.client.login(username='admin', password='testpassword')
        action = self.client.get("/users/" + str(self.user.id) + "/")
        self.assertEqual(action.status_code, 200)

    def test_update_user_no_logging(self):
        action = self.client.get("/users/" + str(self.user.id) + "/edit/")
        self.assertEqual(action.status_code, 302)

    def test_update_user_logging(self):
        self.client.login(username='admin', password='testpassword')
        action = self.client.post("/users/" + str(self.user.id) + "/edit/", {
            'username': 'testuser2',
            'first_name': 'test',
            'last_name': 'user2',
            'iban': 'CH5982876111158263574',
        })
        self.assertEqual(action.status_code, 302)

    def test_delete_user_no_logging(self):
        action = self.client.get("/users/" + str(self.user.id) + "/delete/")
        self.assertEqual(action.status_code, 302)

    def test_delete_user_logging(self):
        self.client.login(username='admin', password='testpassword')
        action = self.client.get("/users/" + str(self.user.id) + "/delete/")
        self.assertEqual(action.status_code, 302)

    def test_delete_user_logging_notcreator(self):
        self.client.login(username='notcreator', password='testpassword')
        action = self.client.get("/users/" + str(self.user.id) + "/delete/")
        self.assertEqual(action.status_code, 302)
