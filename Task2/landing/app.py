from flask import Flask, render_template, request, flash, redirect, url_for
#import flask.scaffold
#flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def addition(num1, num2): 
	#url = 'http://addition-service:'
	url = 'http://127.0.0.1:'
	port = 5051
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']
	
def subtraction(num1, num2): 
	#url = 'http://minus-service:'
	url = 'http://127.0.0.1:'
	port = 5052
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']
	
def multiplication(num1, num2): 
	#url = 'http://multiply-service:'
	url = 'http://127.0.0.1:'
	port = 5053
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']
	
def division(num1, num2): 
	#url = 'http://division-service:'
	url = 'http://127.0.0.1:'
	port = 5054
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']
	
def exponent(num1, num2): 
	#url = 'http://exponent-service:'
	url = 'http://127.0.0.1:'
	port = 5055
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']
	
def lesser_than(num1, num2): 
	#url = 'http://lessthan-service:'
	url = 'http://127.0.0.1:'
	port = 5056
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']
	
def greater_than(num1, num2): 
	#url = 'http://greaterthan-service:'
	url = 'http://127.0.0.1:'
	port = 5057
	add_url = url + str(port) + '/' + str(num1) + '/' + str(num2)
	response = requests.get(add_url)
	print(response)
	return response.json()['result']


@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    
    if number_1 == None or number_2 == None:
    	number_1 = "0"
    	number_2 = "0"
    	
    number_1 = int(number_1)
    number_2 = int(number_2)
    
    if operation == 'add':
        result = addition(number_1, number_2)
    elif operation == 'minus':
        result =  subtraction(number_1, number_2)
    elif operation == 'multiply':
        result = multiplication(number_1, number_2)
    elif operation == 'divide':
        result = division(number_1, number_2)
    elif operation == 'exponent':
        result =  exponent(number_1, number_2)
    elif operation == 'lesser_than':
        result = lesser_than(number_1, number_2)
    elif operation == 'greater_than':
        result = greater_than(number_1, number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
