'''
Created on Nov 14, 2013

@author: siddharth.thole
'''
from pdao import *
import unittest
from user.pdao import get_user_pref, add_user, delete_user


class Test_user_management(unittest.TestCase):

    def test_get_user_credential(self):
        id = input("enter the value for id")
        x = get_user_credential(id)
        self.assertEqual(x, False, 'enter user is valid one')

    def test_get_user_info(self):
        id = input("enter the value for id")
        x = get_user_info(id)
        self.assertEqual(x, False, 'enter user is valid one')

    def test_get_user_pref(self):
        id = input("enter the value for id")
        x = get_user_pref(id)
        self.assertEqual(x, False, 'enter user is valid one')

    def test_get_user_role(self):
        id = input("enter the value for id")
        x = get_user_role(id)
        self.assertEqual(x, False, 'enter user is valid one')

    def test_add_user(self):
        username = input("enter the username")
        password = input("enter the password")
        x = add_user(username,password)
        self.assertEqual(x, True, 'user is added')

    def test_delete_user(self):
        id = input("enter the id")
        x = delete_user(id)
        self.assertEqual(x, True, 'user is deleted')

    def test_edit_user_credential(self):
        user = user_credential()
        id = input("enter the id")
        username = input('enter the username')
        user.username = username
        password = input('enter the password')
        user.password = password
        x = edit_user_credential(id, user)
        self.assertEqual(x, True, 'user edited')

    def test_edit_user_info(self):
        user = user_info()
        id = input("enter the id")
        firstname = input('enter the firstname')
        user.firstname = firstname
        lastname = input('enter the lastname')
        user.lastname = lastname
        x = edit_user_info(id, user)
        self.assertEqual(x, True, 'user edited')

    def test_edit_user_pref(self):
        user = user_pref()
        id = input('enter the id')
        color = input('enter the color')
        user.color = color
        x = edit_user_pref(id, user)
        self.asertEqual(x, True, 'user edited')

    def test_edit_user_role(self):
        user = user_role()
        id = input('enter the id')
        role = input('enter the role')
        user.role = role
        x = edit_user_pref(id, user)
        self.asertEqual(x, True, 'user edited')

    def test_get_user_byusername(self):
        username = input('enter the username')
        password = input('enter the password')
        x = get_user_byusername(username, password)
        self.assertEqual(x, False, 'not a valid user')

    def test_list_all_users(self):
        x = list_all_users()
        self.assertEqual(x, False, 'no users,list is empty')

if __name__ == '__main__':
    unittest.main()