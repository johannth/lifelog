#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask


def create_app(debug=False):
    app = Flask(__name__, static_folder="../static")
    app.debug = debug or os.environ.get("DEBUG") == "True"
    app.secret_key = os.environ["SECRET_KEY"]

    from lifelog.endpoints import api_index

    app.add_url_rule('/', methods=["GET", ], view_func=api_index)

    return app
