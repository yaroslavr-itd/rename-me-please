import flask

import application


class EventJSONEncoder(flask.json.JSONEncoder):

    def default(self, o):
        if isinstance(o, application.events.Event):
            return vars(o)
        return super(EventJSONEncoder, self).default(o)


def file_changed_handler(path_to_file):
    application.events.ACTUAL_EVENTS = application.events.read_events(path_to_file)


def create_app():
    flask_app = flask.Flask(__name__)
    flask_app.json_encoder = EventJSONEncoder
    flask_app.register_blueprint(application.routes.HTTP_API_BLUEPRINT)

    # application.observing.start_observer(
    #     application.observing.PATH_TO_OBSERVE, application.observing.FILE_NAME, file_changed_handler)

    return flask_app
