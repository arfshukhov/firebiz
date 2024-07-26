from origin import *
from middleware.reg_middleware import User

@app.route('/api/auth/registration', methods=['POST'])
def registration():
    fname = User.validate_username(request.json["first_name"])
    lname = User.validate_username(request.json["last_name"])
    password = User.validate_password(request.json["password"])
    email = User.validate_email(request.json["email"])
    country_code = User.validate_country_code(request.json["country_code"])
    phone = User.validate_phone(request.json["phone"])
    if not fname:
        return jsonify({"message": "first name is incorrect"}), 406
    if not lname:
        return jsonify({"message": "last name is incorrect"}), 406
    if not password:
        return jsonify({"message": "password is incorrect"}), 406
    if not email:
        return jsonify({"message": "email is incorrect"}), 406
    if not country_code:
        return jsonify({"message": "country code is incorrect"}), 406
    if not phone:
        return jsonify({"message": "phone is incorrect"}), 406
    new_user = User.register_new(fname,lname, email, password, country_code, phone)
    if new_user:
        return jsonify({
            "message": {
                "first_name": fname,
                "last_name": lname,
                "email": email,
                
            }
        })