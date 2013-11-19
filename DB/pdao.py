'''
Created on Nov 14, 2013

@author: siddharth.thole
'''
from peewee import *

db = MySQLDatabase("user_management", user="root", passwd="root", host="127.0.0.1", port=3306)


class UserCredential(Model):
    id = PrimaryKeyField()
    username = CharField()
    password = CharField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    class Meta:
        database = db

#UserCredential table structure where id act as primary_key,database here is user_management


class UserInfo(Model):
    id1 = ForeignKeyField(UserCredential)
    firstname = CharField()
    lastname = CharField()
    phone1 = CharField()
    phone2 = CharField()
    primary_email = CharField()
    email = CharField()
    address_line1 = CharField()
    address_line2 = CharField()
    pin = IntegerField()
    country = CharField()
    image = BlobField()

    class Meta:
        database = db

#UserInfo table structure where id1 is foreign_key


class UserPref(Model):
    id2 = ForeignKeyField(UserCredential)
    color = CharField()
    decimal = CharField()
    currency = CharField()
    time_format = CharField()
    date_format = CharField()

    class Meta:
        database = db

#UserPref table structure where id2 is foreign_key


class UserRole(Model):
    id3 = ForeignKeyField(UserCredential)
    role = CharField()

    class Meta:
        database = db

#UserRole table structure where id3 is foreign key


def get_user_credential(id):
    try:
        user = UserCredential.get(UserCredential.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_credential function  returns the user object with the given id


def get_user_info(id):
    try:
        user = UserInfo.get(UserInfo.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_info function  returns the user object with the given id


def get_user_pref(id):
    try:
        user = UserPref.get(UserPref.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_pref function  returns the user object with the given id


def get_user_role(id):
    try:
        user = UserRole.get(UserRole.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_role function  returns the user object with the given id


def add_user(username1, password1):
    try:
        user1 = UserCredential.create(username = username1, password = password1)
        user2 = UserInfo.create(id = user1.id)
        user3 = UserPref.create(id = user1.id)
        user4 = UserRole.create(id = user1.id)

    except:
        return 'Username already present'

    else:
        return True


#add the given user to the UserCredential table and create entry in all other table with same id


def delete_user(id):
    try:
        user = UserCredential.get(UserCredential.id == id)
        user1 = UserInfo.get(UserInfo.id == id)
        user2 = UserPref.get(UserPref.id == id)
        user3 = UserRole.get(UserRole.id == id)

    except DoesNotExist:
        return False

    else:
        user.delete_instance()
        user1.delete_instance()
        user2.delete_instance()
        user3.delete_instance()
        return True

#delete_user function takes id as input and delete the record of given id from all the tables


def edit_user_credential(id, user):
    try:
        user1 = UserCredential.get(UserCredential.id == id)

    except DoesNotExist:
        return False

    else:
        if user.username and user.password != '':
            user1.username = user.username
            user1.password = user.password
        else:
            return 'Username or Password cannot be null'

        user1.save()
        return True

#In edit_user_credential function,id and user object is taken as input and the username and password of the user with given id is changed


def edit_user_info(id, user):
    try:
        user1 = UserInfo.get(UserInfo.id == id)

    except DoesNotExist:
        return False

    else:
        if user.firstname != '':
            user1.firstname = user.firstname
        else:
            return 'firstname cannot be null'

        if user.lastname != '':
            user1.lastname = user.lastname
        else:
            return 'lastname cannot be null'

        user1.phone1 = user.phone1
        user1.phone2 = user.phone2

        if user.primary_email != '':
            user1.primary_email = user.primary_email
        else:
            return 'Primary email cannot be null'

        user1.email = user.email
        user1.address_line1 = user.address_line1
        user1.address_line2 = user.address_line2

        if user.pin == None:
            return 'Pin cannot be null'
        else:
            if isinstance(user.pin, int):
                s = str(user.pin)
                l = len(s)
                user.pin = int(s, 0)
                if l <= 8:
                    user1.pin = user.pin
                else:
                    return 'Pin is too long'
            else:
                return 'Pin must be in numbers'

        if user.country == '':
            return 'Country cannot be null'
        else:
            if len(user.country) <= 3:
                user1.firstname = user.firstname
            else:
                return 'Country code is too long'

        user1.image = user.image

        user1.save()
        return True

#in edit_user_info function,id and user object is taken as input and the attributes which are updated of the user with given id is changed


def edit_user_pref(id, user):
    try:
        user1 = UserPref.get(UserPref.id == id)

    except DoesNotExist:
        return False
    else:
        if user.color != '':
            user1.color = user.color
        else:
            return 'Color cannot be null'

        if len(user.decimal) <= 2:
            user1.decimal = user.decimal
        else:
            return 'Data too long'

        if len(user.currency) <= 2:
            user1.currency = user.currency
        else:
            return 'Data too long'

        user1.time_format = user.time_format
        user1.date_format = user.date_format

        user1.save()
        return True


#in edit_user_pref function,id and user object is taken as input and the attributes which are updated of the user with given id is changed


def edit_user_role(id, role):
    try:
        user1 = UserRole.get(UserRole.id == id)

    except DoesNotExist:
        return False
    else:
        if role != '':
            if role == 'Admin' or role == 'User':
                user1.role = role
            else:
                return 'There can be only two role: Admin and User '
        else:
            return 'role cannot be null'
        user1.save()
        return True

#in edit_user_role,id and user object is taken as input and the attributes which are updated of the user with given id is changed


def get_user(username, password):
    try:
        user = UserCredential.get(UserCredential.username == username)

        if user.password != password:
            return False

    except DoesNotExist:
        return False

    else:
        return user

#get_user_byusername function takes username and password as input and returns the object of UserCredential with same username and password


def get_user_by_username(username):
    try:
        user = UserCredential.get(UserCredential.username == username)

    except DoesNotExist:
        return False

    else:
        return user




def list_all_users():
    user_list = []
    try:
        for user in UserCredential.select():
            user_list.append(user)

    except:
        return False

    else:
        return user_list

#list_all_user returns the list of all users
