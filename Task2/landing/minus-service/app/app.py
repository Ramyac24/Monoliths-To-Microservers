from flask import Flask, jsonify, request
#import flask.scaffold
#flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):

	def get(self):

		return jsonify({'message': 'hello world'})

	def post(self):
		
		data = request.get_json()	 
		return jsonify({'data': data}), 200



class Subtract(Resource):

	def get(self, num1,num2):

		return jsonify({'subtraction result': num1-num2})


api.add_resource(Hello, '/')
api.add_resource(Subtract, '/<int:num1>/<int:num2>')

# subtraction  use url/sub/6/4


if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5052)
