# -*- coding: utf-8 -*-

__author__ = 'DavidWCaraway'

from flask.ext.restful import abort
from app.models.model import user
from app.api.base import BaseView, secure_endpoint

class UsersView(BaseView):

    def index(self):
        abort(501) #TODO implement

    @secure_endpoint()
    def post(self):
        abort(501) #TODO implement

    def get(self, id):
        abort(501) #TODO implement

    @secure_endpoint()
    def put(self, email, password):
        user = User(email=email, password=password)
        user.save()
        return dict(id=user.id)

    @secure_endpoint()
    def delete(self, id):
        abort(501) #TODO implement
