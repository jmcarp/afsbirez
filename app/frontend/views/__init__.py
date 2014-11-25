# -*- coding: utf-8 -*-                                                                                       
"""
    frontend.views
    ~~~~~~~~~~~~~~

    :author: 18F
    :copyright: © 2014-2015, 18F
    :license: CC0 Public Domain License, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
from .auth import AuthView
from .legal import LegalView
from .todos import TodosView

def init_app(app):
    AuthView.register(app)
    LegalView.register(app)
    TodosView.register(app)