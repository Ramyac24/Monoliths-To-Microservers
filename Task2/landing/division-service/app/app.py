from flask import Flask, render_template, request, flash, redirect, url_for
#import flask.scaffold
#flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse

import requests
import os


class DivisionService(Resource):
    def get(self, argument0, argument1):
        return argument0 / argument1, 200

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

api = Api(app)
api.add_resource(DivisionService, '/<int:argument0>/<int:argument1>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5054,
        host="0.0.0.0"
    )
