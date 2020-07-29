import datetime
import logging

from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource, Api

from sif.model.user import User

bp = Blueprint('auth', __name__)
api = Api(bp)


@api.resource('/signup')
class SignupApi(Resource):
    def post(self):
        logging.info("Sign up user.")
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200


@api.resource('/login')
class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
