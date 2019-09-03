from flask import Flask, jsonify, request
from flask_socketio import SocketIO

app.config['SECRET_KEY'] = 'secret!'
app = Flask(__name__)
socketio = SocketIO(app)

users = [
			{
				'id' : 1,
				'name' : 'Person 1',
				'age' : 21
			},
			{
				'id' : 2,
				'name' : 'Person 2',
				'age' : 18
			},
			{
				'id' : 3,
				'name' : 'Person 3',
				'age' : 22
			}

]

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/users')            # decorator
def get_users():
	return jsonify(users)

@app.route('/users/<id>')
def get_user(id):
	list(filter(lambda u: u['id']==id,users))
	return jsonify(user)
	
# install socket:
'''
	pip install flask-socketio
	this is for real time update
'''
# open the page for documentation https://flask-socketio.readthedocs.io/en/latest


@socketio.on('message')
def handle_message(data):
	socketio.emit('push',data,broadcast=True,include_sef=False)

if __name__ == "__main__":
	socketio.run(app)










