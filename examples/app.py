# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Minimal Flask application example.

First install Invenio-Archivematica, setup the application and load
fixture data by running:

.. code-block:: console

   $ pip install -e .[all]
   $ cd examples
   $ ./app-setup.sh
   $ ./app-fixtures.sh

Next, start the development server:

.. code-block:: console

   $ export FLASK_APP=app.py FLASK_DEBUG=1
   $ flask run

and open the example application in your browser:

.. code-block:: console

    $ open http://127.0.0.1:5000/

To reset the example application run:

.. code-block:: console

    $ ./app-teardown.sh
"""

from __future__ import absolute_import, print_function

import os

from flask import Flask
from flask_babelex import Babel
from invenio_access import InvenioAccess
from invenio_accounts import InvenioAccounts
from invenio_db import InvenioDB
from invenio_files_rest import InvenioFilesREST
from invenio_pidstore import InvenioPIDStore
from invenio_rest import InvenioREST
from invenio_sipstore import InvenioSIPStore

from invenio_archivematica import InvenioArchivematica
from invenio_archivematica.views.ui import blueprint

# Create Flask application
app = Flask(__name__)
app.config.update(dict(
    BROKER_URL='redis://',
    CELERY_RESULT_BACKEND='redis://',
    REST_ENABLE_CORS=True,
    SECRET_KEY='CHANGEME',
    SIPSTORE_AGENT_JSONSCHEMA_ENABLED=False,
    SQLALCHEMY_ECHO=False,
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db'
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
))

Babel(app)
InvenioAccess(app)
InvenioAccounts(app)
InvenioArchivematica(app)
InvenioDB(app)
InvenioFilesREST(app)
InvenioPIDStore(app)
InvenioREST(app)
InvenioSIPStore(app)

app.register_blueprint(blueprint)
