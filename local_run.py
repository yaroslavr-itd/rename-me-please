import os

import aren_csv_app

HOST = os.getenv('ARENCSV_HOST', 'localhost')
PORT = os.getenv('ARENCSV_PORT', 8080)
DEBUG = os.getenv('ARENCSV_DEBUG', True)

APP = aren_csv_app.create_app()

APP.run(aren_csv_app.FLASK_APP, HOST, PORT, debug=DEBUG)