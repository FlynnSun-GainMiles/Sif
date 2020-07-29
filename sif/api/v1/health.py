import logging

from flask import Blueprint
from flask_cors import cross_origin
from flask_restful import Api, Resource


bp = Blueprint('health', __name__)
api = Api(bp)


@api.resource('/hc')
class HealthCheck(Resource):
    @staticmethod
    def __name__():
        return 'HealthCheck'

    @cross_origin()
    def get(self):
        logging.info("Google Cloud Health Check Api")
        return {
            'message': '{}: This endpoint for GCP health check'.format(self.__name__())
        }, 200


