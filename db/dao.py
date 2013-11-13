'''
Created on Nov 11, 2013

@author: siddharth.thole
'''

from peewee import *

db = MySQLDatabase("credits",user = "root", passwd = "root", host="127.0.0.1",port=3306)

class user(Model):
                
            username = CharField()
            password = CharField()
            role=CharField()
            color=CharField()
                
            class Meta:
                database = db
        


    
def Delete_User(id):
    try:        
        user1 = user.get(user.id==id)              
        user1.delete_instance()
    
    except DoesNotExist:
        return False
    
    else:
        return True            


def Get_User(id):
    try:                         
        user1 = user.get(user.id==id)              
        
    
    except DoesNotExist:
        return False
    else:
        return user1      


def Add_User(user1):
    try:
        user2 = user.create(username=user1.username, password=user1.password,role=user1.role,color=user1.color)
    
    except:
        return False
    else:
        return True


def Edit_User(id,user1):
    try:
        user2 = user.get(user.id==id)
 
    except DoesNotExist:
        return False
    else:
        if user1.username!=None and user1.username!=user2.username:       
            user2.username=user1.username
        if user1.password!=None and user1.username!=user2.username:
            user2.password=user1.password
        if user1.color!=None and user1.username!=user2.username:
            user2.color=user1.color
        if user1.role!=None and user1.username!=user2.username:
            user2.role=user1.role
        user2.save()
        return True
        
                       
    
def Get_User_ByUsername(username1,password1):
    try:
        user1 = user.get(user.username==username1,user.password==password1)
        
    except DoesNotExist:
        return False
    else:
        return user1    
    
    
  
def List_All_User():
    i=0
    user_list=[]
    
    
    for user1 in user.select():
            user_list.append(user1)
            i = i+1         
    return user_list
