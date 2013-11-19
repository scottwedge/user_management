'''
Created on Nov 14, 2013

@author: siddharth.thole
'''
from peewee import *

db = MySQLDatabase("user_management", user="root", passwd="root", host="127.0.0.1", port=3306)


class user_credential(Model):
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

#user_credential table structure where id act as primary_key,database here is user_management


class user_info(Model):
    id1 = ForeignKeyField(user_credential)
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

#user_info table structure where id1 is foreign_key


class user_pref(Model):
    id2 = ForeignKeyField(user_credential)
    color = CharField()
    decimal = CharField()
    currency = CharField()
    time_format = CharField()
    date_format = CharField()

    class Meta:
        database = db

#user_pref table structure where id2 is foreign_key


class user_role(Model):
    id3 = ForeignKeyField(user_credential)
    role = CharField()

    class Meta:
        database = db

#user_role table structure where id3 is foreign key


def get_user_credential(id):
    try:
        user = user_credential.get(user_credential.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_credential function  returns the user object with the given id


def get_user_info(id):
    try:
        user = user_info.get(user_info.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_info function  returns the user object with the given id


def get_user_pref(id):
    try:
        user = user_pref.get(user_pref.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_pref function  returns the user object with the given id


def get_user_role(id):
    try:
        user = user_role.get(user_role.id == id)

    except DoesNotExist:
        return False

    else:
        return user

#get_user_role function  returns the user object with the given id


def add_user(username1, password1):
    try:
        user1 = user_credential.create(username = username1, password = password1)
        user2 = user_info.create(id = user1.id)
        user3 = user_pref.create(id = user1.id)
        user4 = user_role.create(id = user1.id)

    except:
        return False

    else:
        return True


#add the given user to the user_credential table and create entry in all other table with same id


def delete_user(id):
    try:
        user = user_credential.get(user_credential.id == id)
        user1 = user_info.get(user_info.id == id)
        user2 = user_pref.get(user_pref.id == id)
        user3 = user_role.get(user_role.id == id)

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
        user1 = user_credential.get(user_credential.id == id)

    except DoesNotExist:
        return False

    else:
        if user.username != None and user.username != user1.username:
            user1.username = user.username

        if user.password != None and user.password != user1.password:
            user1.password = user.password

        user1.save()
        return True


#In edit_user_credential function,id and user object is taken as input and the username and password of the user with given id is changed


def edit_user_info(id, user):
    try:
        user1 = user_info.get(user_info.id == id)

    except DoesNotExist:
        return False

    else:
        if user1.firstname and user1.lastname and user1.phone1 and user1.phone2 and user1.primary_email and user1.email and user1.address_line1 and user1.address_line2 and user1.pin and user1.country and user1.image == None:
            user1.firstname = user.firstname
            user1.lastname = user.lastname
            user1.phone1 = user.phone1
            user1.phone2 = user.phone2
            user1.primary_email = user.primary_email
            user1.email = user.email
            user1.address_line1 = user.address_line1
            user1.address_line2 = user.address_line2
            user1.pin = user.pin
            user1.country = user.country
            user1.image = user.image

        else:
            if user.firstname != None and user.firstname != user1.firstname:
                user1.firstname = user.firstname

            if user.lastname != None and user.lastname != user1.lastname:
                user1.lastname = user.lastname

            if user.phone1 != None and user.phone1 != user1.phone1:
                user1.phone1 = user.phone1

            if user.phone2 != None and user.phone2 != user1.phone2:
                user1.phone2 = user.phone2

            if user.primary_email != None and user.primary_email != user1.primary_email:
                user1.primary_email = user.primary_email

            if user.email != None and user.email != user1.email:
                user1.email = user.email

            if user.address_line1 != None and user.address_line1 != user1.address_line1:
                user1.address_line1 = user.address_line1

            if user.address_line2 != None and user.address_line2 != user1.address_line2:
                user1.address_line2 = user.address_line2

            if user.pin != None and user.pin != user1.pin:
                user1.pin = user.pin

            if user.country != None and user.country != user1.country:
                user1.country = user.country

            if user.image != None and user.image != user1.image:
                user1.image = user.image

        user1.save()
        return True

#in edit_user_info function,id and user object is taken as input and the attributes which are updated of the user with given id is changed


def edit_user_pref(id, user):
    try:
        user1 = user_pref.get(user_pref.id == id)

    except DoesNotExist:
        return False
    else:

        if user1.color and user1.decimal and user1.currency and user1.time_format and user1.date_format == None:
            user1.color = user.color
            user1.decimal = user.decimal
            user1.currency = user.currency
            user1.time_format = user.time_format
            user1.date_format = user.date_format

        else:
            if user.color != None and user.color != user1.color:
                user1.color = user.color

            if user.decimal != None and user.decimal != user1.decimal:
                user1.decimal = user.decimal

            if user.currency != None and user.currency != user1.currency:
                user1.currency = user.currency

            if user.time_format != None and user.time_format != user1.time_format:
                user1.time_format = user.time_format

            if user.date_format != None and user.date_format != user1.date_format:
                user1.date_format = user.date_format

        user1.save()
        return True


#in edit_user_pref function,id and user object is taken as input and the attributes which are updated of the user with given id is changed


def edit_user_role(id, role):
    try:
        user1 = user_role.get(user_role.id == id)

    except DoesNotExist:
        return False
    else:

        if user1.role is None:
            user1.role = role
        else:
            if user1.role != role and role != None:
                user1.role = role

        user1.save()
        return True

#in edit_user_role,id and user object is taken as input and the attributes which are updated of the user with given id is changed


def get_user(username, password):
    try:
        user = user_credential.get(user_credential.username == username)

        if user.password != password:
            return False

    except DoesNotExist:
        return False

    else:
        return user

#get_user_byusername function takes username and password as input and returns the object of user_credential with same username and password


def get_user_by_username(username):
    try:
        user = user_credential.get(user_credential.username == username)

    except DoesNotExist:
        return False

    else:
        return user




def list_all_users():
    user_list = []
    try:
        for user in user_credential.select():
            user_list.append(user)

    except:
        return False

    else:
        return user_list

#list_all_user returns the list of all users
