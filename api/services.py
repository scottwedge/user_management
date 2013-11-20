'''
Created on Nov 14, 2013

@author: manish.meshram
'''
from flask import Flask, jsonify
from flask import request, abort
from pdao import *
from flask_login import LoginManager, login_required, login_user, logout_user


app = Flask(__name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
    return get_user_credential(userid)


@app.route('/login', methods=['POST'])
def login():
    """Login method"""
    if not request.json:
        abort(400)

    username = request.json['username']
    password = request.json['password']

    #temporary dictionary which we will send as response
    temp_dict = {}

    #storing status as INVALID
    temp_dict['status'] = 'INVALID'

    #getting user credentials object by username and password
    user_cred = get_user(username, password)

    if user_cred != False:

        #getting user preference object by id
        user_pref = get_user_pref(user_cred.id)
        if user_pref == False:
            return jsonify({'user': temp_dict})
        else:
            #adding 'color' in temporary dictionary
            temp_dict["color"] = user_pref.color

        #getting user role object by id
        user_role = get_user_role(user_cred.id)
        if user_role == False:
            return jsonify({'user': temp_dict})
        else:
            #adding 'color' in temporary dictionary
            temp_dict["role"] = user_role.role

        #adding 'id' in temporary dictionary
        temp_dict["id"] = user_cred.id

        #adding 'username' in temporary dictionary
        temp_dict["username"] = user_cred.username

        login_user(user_cred)

        temp_dict['status'] = 'SUCCESS'

    return jsonify({'user': temp_dict})


@app.route('/get_users', methods=['GET'])
@login_required
def get_users():
    """Method for getting all the users present"""
    user_creds_list = list_all_users()

    if len(user_creds_list) == 0:
        return jsonify({'status': 'NO USERS AVAILABLE'})

    all_users_list = []

    for user_cred in user_creds_list:
        temp_dict = {}

        temp_dict['id'] = user_cred.id

        user_info = get_user_info(user_cred.id)
        temp_dict['firstname'] = user_info.firstname
        temp_dict['lastname'] = user_info.lastname

        user_role = get_user_role(user_cred.id)
        temp_dict['role'] = user_role.role

        all_users_list.append(temp_dict)

    return jsonify({'users': all_users_list})


@app.route('/delete_user/<user_id>', methods=['DELETE'])
@login_required
def delet_user(user_id):
    """Method for delete user.Given the name as delet because our DAO layer
    method name is delete_user"""
    status = delete_user(user_id)

    if status == True:
        return jsonify({'status': 'SUCCESS'})
    return jsonify({'status': 'INVALID USER ID'})


@app.route('/get_user/<username>', methods=['GET'])
@login_required
def get_user_api(username):
    """Method for getting full information of User
    by using its username which is unique.
    Responses:
    INVALID USERNAME - your given username is not present
    USER INFO NOT PRESENT - user_info is not available
                            for required username
    USER PREF NOT PRESENT - user_pref is not available
                            for required username"""

    #temporary directory we will send as response
    temp_dict = {}

    user_cred = get_user_by_username(username)

    if user_cred == False:
        return jsonify({'status': 'INVALID USERNAME'})
    else:
        temp_dict['id'] = user_cred.id

        #getting user_info
        user_info = get_user_info(user_cred.id)

        if user_info == False:
            return jsonify({'status': 'USER INFO NOT PRESENT'})
        else:
            temp_dict['firstname'] = user_info.firstname
            temp_dict['lastname'] = user_info.lastname
            temp_dict['phone1'] = user_info.phone1
            temp_dict['phone2'] = user_info.phone2
            temp_dict['primary_email'] = user_info.primary_email
            temp_dict['email'] = user_info.email
            temp_dict['address_line1'] = user_info.address_line1
            temp_dict['address_line2'] = user_info.address_line2
            temp_dict['pin'] = user_info.pin
            temp_dict['country'] = user_info.country

        #getting user_pref
        user_pref = get_user_pref(user_cred.id)

        if user_pref == False:
            return jsonify({'status': 'USER PREF NOT PRESENT'})
        else:
            temp_dict['color'] = user_pref.color
            temp_dict['decimal'] = user_pref.decimal
            temp_dict['currency'] = user_pref.currency
            temp_dict['time_format'] = user_pref.time_format
            temp_dict['date_format'] = user_pref.date_format

        #if 'admin' is logged in then only he will see the role field
        '''
        logged_in_user_role = get_user_role(current_user_id)

        if logged_in_user_role == False:
            return jsonify({'status': 'INVALID USER ID'}), 406
        elif logged_in_user_role.role == 'Admin':

            user_role = get_user_role(user_cred.id)

            if user_role == False:
                return jsonify({'status': 'USER ROLE NOT PRESENT'}), 406
            elif user_role.role != 'Admin':
                temp_dict['role'] = user_role.role'''

    return jsonify({'user': temp_dict})


@app.route('/add_user', methods=['POST'])
@login_required
def add_user_api():
    """Add objects for user_pref, user_info and user_role"""
    if not request.json:
        abort(400)

    temp_user_id = request.json['id']
    temp_user_role = request.json['role']

    status = edit_user_role(temp_user_id, temp_user_role)

    if status == False:
        return jsonify({'status': 'INVALID USER ID'})
    elif status == True:
        return update_user_api()
    else:
        return jsonify({'status': status})


@app.route('/update_user', methods=['PUT'])
@login_required
def update_user_api():
    """Method for updating full information of User
    Responses:"""

    status = edit_user_pref_method()

    if status == False:
        return jsonify({'status': 'INVALID USER ID'})
    elif status == True:

        """We will do further operations if status == True
        i.e. user_pref object is updated in DB"""
        status = edit_user_info_method()

        if status == False:
            return jsonify({'status': 'INVALID USER ID'})
        elif status == True:
            return jsonify({'status': 'SUCCESS'})
        else:
            return jsonify({'status': status})
    else:
        return jsonify({'status': status})

    '''
    logged_in_user_role = get_user_role(current_user_id)

    if logged_in_user_role == False:
        return jsonify({'status': 'INVALID USER ID'}), 406
    elif logged_in_user_role.role == 'Admin':
        temp_user_role = UserRole()
        temp_user_role.id = request.json['id']
        temp_user_role.role = request.json['role']

        edit_user_role(temp_user_role.id, temp_user_role)
    '''
    return jsonify({'status': 'SUCCESS'})




@app.route('/get_user_info/<user_id>', methods=['GET'])
@login_required
def get_user_info_api(user_id):
    """Method for getting user_info object of given user_id"""
    user_info = get_user_info(user_id)

    #Dictionary for storing info data about required user
    #This list will get sent as a response after converting it into json
    temp_dict = {}

    if user_info == False:
        return "INVALID ID", 406
    else:
        temp_dict['firstname'] = user_info.firstname
        temp_dict['lastname'] = user_info.lastname
        temp_dict['phone1'] = user_info.phone1
        temp_dict['phone2'] = user_info.phone2
        temp_dict['primary_email'] = user_info.primary_email
        temp_dict['email'] = user_info.email
        temp_dict['address_line1'] = user_info.address_line1
        temp_dict['address_line2'] = user_info.address_line2
        temp_dict['pin'] = user_info.pin
        temp_dict['country'] = user_info.country

        return jsonify({'user_info': temp_dict})


@app.route('/get_user_pref/<user_id>', methods=['GET'])
@login_required
def get_user_pref_api(user_id):
    """Method for getting user_pref object """
    user_pref = get_user_pref(user_id)

    temp_dict = {}

    if user_pref == False:
        return "INVALID ID", 406
    else:
        temp_dict['color'] = user_pref.color
        temp_dict['decimal'] = user_pref.decimal
        temp_dict['currency'] = user_pref.currency
        temp_dict['time_format'] = user_pref.time_format
        temp_dict['date_format'] = user_pref.date_format

        return jsonify({'user_pref': temp_dict})


@app.route('/update_user_info', methods=['PUT'])
@login_required
def update_user_info_api():
    """Method for updating user_info object """
    if not request.json:
        abort(400)

    status = edit_user_info_method()

    if status == True:
        return "updated"
    else:
        return "INVALID ID", 406


@app.route('/update_user_pref', methods=['PUT'])
@login_required
def update_user_pref_api():
    """Method for updating user_pref object """
    if not request.json:
        abort(400)

    status = edit_user_pref_method()

    if status == True:
        return "updated"
    else:
        return "", 406


@app.route('/add_user_creds', methods=['POST'])
@login_required
def add_user_creds_api():
    """Method for adding user credentials"""
    if not request.json:
        abort(400)

    username = request.json['username']
    password = request.json['password']

    created_user_id = add_user(username, password)

    if isinstance(created_user_id, basestring):
        return jsonify({'status': created_user_id})
    else:
        return jsonify({'user_id': created_user_id})


@app.route('/add_user_pref', methods=['PUT'])
@login_required
def add_user_pref_api():
    """Method for adding user pref"""
    if not request.json:
        abort(400)

    status = edit_user_pref_method()

    if status == True:
        return jsonify({"status": "SUCCESS"})
    else:
        return "", 406


@app.route('/add_user_info', methods=['PUT'])
@login_required
def add_user_info_api():
    """Method for adding user info"""
    #print request
    if not request.json:
        abort(400)

    status = edit_user_info_method()

    if status == True:
        return jsonify({"status": "SUCCESS"})
    else:
        return "", 406


@app.route('/add_user_role', methods=['PUT'])
@login_required
def add_user_role_api():
    """Method for adding user role"""
    if not request.json:
        abort(400)

    user_id = request.json['id']
    user_role = request.json['role']

    status = edit_user_role(user_id, user_role)

    if status == True:
        return jsonify({"status": "SUCCESS"})
    elif status == False:
        return jsonify({"status": "INVALID USER ID"})
    else:
        return jsonify({"status": status})


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Logout method"""

    logout_user()
    return jsonify({"status": "SUCCESS"})


@app.route('/change_password', methods=['PUT'])
@login_required
def change_password():
    """Change password method"""
    if not request.json:
        abort(400)

    user_id = request.json['id']
    old_password = request.json['old_password']

    user_cred = get_user_credential(user_id)

    if user_cred == False:
        return jsonify({"status": "INVALID USER ID"})
    else:
        if user_cred.password != old_password:
            return jsonify({"status": "INCORRECT OLD PASSWORD"})
        else:
            new_password = request.json['new_password']

            temp_user_cred = UserCredential()
            temp_user_cred.id = user_id
            temp_user_cred.username = user_cred.username
            temp_user_cred.password = new_password

            status = edit_user_credential(temp_user_cred.id, temp_user_cred)

            if status == True:
                return jsonify({"status": "SUCCESS"})
            elif status == False:
                return jsonify({"status": "INVALID USER ID"})
            else:
                return jsonify({"status": "PASSWORD CANNOT BE NULL"})


"""General methods"""


def edit_user_pref_method():
    """This is generalized method for editing user_pref
    Made it generalized beacuse it is being called from multiple places"""
    temp_user_pref = UserPref()

    temp_user_pref.id = request.json['id']
    temp_user_pref.color = request.json['color']
    temp_user_pref.decimal = request.json['decimal']
    temp_user_pref.currency = request.json['currency']
    temp_user_pref.time_format = request.json['time_format']
    temp_user_pref.date_format = request.json['date_format']

    status = edit_user_pref(temp_user_pref.id, temp_user_pref)

    return status


def edit_user_info_method():
    """This is generalized method for editing user_info
    Made it generalized beacuse it is being called from multiple places"""

    temp_user_info = UserInfo()

    temp_user_info.id = request.json['id']
    temp_user_info.firstname = request.json['firstname']
    temp_user_info.lastname = request.json['lastname']
    temp_user_info.phone1 = request.json['phone1']
    temp_user_info.phone2 = request.json['phone2']
    temp_user_info.primary_email = request.json['primary_email']
    temp_user_info.email = request.json['email']
    temp_user_info.address_line1 = request.json['address_line1']
    temp_user_info.address_line2 = request.json['address_line2']
    temp_user_info.pin = request.json['pin']
    temp_user_info.country = request.json['country']

    status = edit_user_info(temp_user_info.id, temp_user_info)

    return status


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    login_manager.init_app(app)
    app.run(debug=True, host="0.0.0.0")
