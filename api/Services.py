'''
Created on Nov 12, 2013

@author: manish.meshram
'''
from flask import Flask, jsonify, session, make_response
from flask import request, abort
from Dao import *
from os import urandom
from random import randint

app = Flask(__name__)


'''---LOGIN---'''
@app.route('/login', methods = ['POST'])
def login():
    if not request.json:
        abort(400)
    
    username = request.json['username']
    password = request.json['password']
    
    user = Get_User_ByUsername(username,password)
    
    j_user = {}
    
    if user == False:
        j_user['status']='ERROR'
    else:
        j_user['status']='SUCCESS'    
        
        j_user['userid']= user.id
        j_user['username']= user.username
        j_user['role']= user.role
        j_user['color']= user.color
        
    return jsonify( { 'response': j_user } )

    
    
'''---CREATE USER---'''
@app.route('/create_user', methods = ['POST'])
def create_user():
    if not request.json:
        abort(400)
    
    myUser = user()
    
    myUser.username = request.json['username']
    myUser.password = request.json['password']
    myUser.role = request.json['role']
    myUser.color = request.json['color']
    
    booln = Add_User(myUser)
    
    res = {}
    if booln == True:
        res['status']='SUCCESS'
    else:
        res['status']='ERROR'
        
    return jsonify( { 'response': res } ), 201


'''---LOGOUT---'''
@app.route('/logout', methods = ['GET'])
def logout():
    res = {
           'status' : 'SUCCESS' 
           }
    return jsonify( { 'response': res } ) 



'''---GET USER---'''
@app.route('/get_user', methods = ['POST'])
def get_user():
    user_id = request.json['userid']
    user = Get_User(user_id)
    
    j_user = {}
    
    if user == False:
        j_user['status']='ERROR'
    else:
        j_user['status']='SUCCESS'    
        
        j_user['user1']={
                         'id':user.id,
                         'username':user.username,
                         'role':user.role,
                         'color':user.color
                         }
        
    return jsonify( { 'response': j_user } )


'''---DELETE USER---'''
@app.route('/delete_user', methods = ['DELETE'])
def delete_user():
    user_id = request.json['userid']
    booln = Delete_User(user_id)
    
    res = {}
    if booln == True:
        res['status']='SUCCESS'
    else:
        res['status']='ERROR'
        
    return jsonify( { 'response': res } )
        

'''---EDIT USER---'''
@app.route('/edit_user', methods = ['PUT'])
def edit_user():
    user_id = request.json['userid']
    temp_user = user()
    
    temp_user.color = request.json['color']
    temp_user.password = request.json['password']
    
    booln = Edit_User(user_id,temp_user)
    
    res = {}
    if booln == True:
        res['status']='SUCCESS'
    else:
        res['status']='ERROR'
        
    return jsonify( { 'response': res } )



'''---GET ALl USERS---'''
@app.route('/get_users', methods = ['GET'])
def get_users():
    user_list = List_All_User()
    print user_list
    
    #user = Get_User(user_id)
    
    j_users = {}
 
    if user_list == False:
        j_users['status']='ERROR'
    else:
        j_users['status']='SUCCESS'    
        
        i = 1
        for obj in user_list:
            j_users['user'+str(i)]={
                                    'id':obj.id,
                                    'username':obj.username,
                                    'role':obj.role,
                                    'color':obj.color
                                    }
            i += 1
        
    return jsonify( { 'response': j_users } )
    
    
    
    


'''
Below route is for testing purpose only and will be removed.
When user will login for the first time this method will get called,
it will generate a random no and use it as session id.
It will send that random no in response as a cookie.

We will use this type of method only during logging in
'''
@app.route('/login_test', methods = ['GET'])
def login_test():
    """Login Test"""
    ip_address = request.remote_addr
    print "IP is: "+ip_address
    generatedRandomNo = urandom(25)
    #randint(1000,10000)
    session[ip_address] = generatedRandomNo
    
    print generatedRandomNo
    print session
    
    resp = make_response()
    resp.set_cookie('cook',generatedRandomNo)
    return resp


'''
Below route is for testing purpose only and will be removed.
It will check whether user is logged in or not.

We will use this type of method when admin/user is logged in and
if he/she wants to perform any operations like edit,delete,etc
'''
@app.route('/login_check', methods = ['GET'])
def login_check():
    ip_address = request.remote_addr
    print "IP is: "+ip_address
    if ip_address in session:
        return "You are logged in"
    else:
        return "Please login first"

'''
Below route is for testing purpose only and will be removed.
It will delete the session variable we are maintaing.

We will use this method during logout
'''
@app.route('/logout_test', methods = ['GET'])
def logout_test():
    ip_address = request.remote_addr
    print "IP is: "+ip_address
    if ip_address in session:
        session.pop(ip_address, None)
        return "You are logged out successfully.."
    else:
        return "Please are not logged in"
    
    

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug = True, host="0.0.0.0")
