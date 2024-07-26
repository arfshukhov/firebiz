from origin import *
from middleware.reg_middleware import *

@app.route('/')
def hello_world():  # put application's code here
    return str(User.validate_username("9арионов"))


@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run()
