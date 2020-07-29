import logging

from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, Api

from sif.model.orm import get_movie, get_all_movie
from sif.model.user import User

bp = Blueprint('movie', __name__)
api = Api(bp)


@api.resource('/movie/<title>')
class Movie(Resource):
    @staticmethod
    def __name__():
        return 'Movie'

    @cross_origin()
    @jwt_required
    def get(self, title):
        logging.info("Get movie info")
        queryset = get_movie(title)
        if len(queryset) > 0:
            return {
                'message': 'This endpoint for query movie',
                'data': queryset.to_json()
            }, 200
        else:
            return {
                'message': 'This endpoint for query movie',
                'error': 'Can not found movie'
            }, 404


@api.resource('/movie/')
class MovieAll(Resource):
    @staticmethod
    def __name__():
        return 'MovieAll'

    @cross_origin()
    @jwt_required
    def get(self):
        logging.info("Get all movie")
        movie = get_all_movie()
        return {
                   'message': 'This endpoint for query all movie',
                   'data': movie.to_json()
               }, 200

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        movie = Movie(**body, added_by=user)
        movie.save()
        user.update(push__movies=movie)
        user.save()
        movie_id = movie.id
        return {'id': str(movie_id)}, 200
