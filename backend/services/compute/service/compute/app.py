import json
import os

from flask import Flask, make_response, g
from flask_restful import Api
from werkzeug.contrib.cache import SimpleCache
from lib.util import init_env
from resources import RootResource, TasksResource, TaskResource, PipelinesResource

app = Flask(__name__)

if os.getenv('COMPUTE_SERVICE_SETTINGS', None) is None:
    os.environ['COMPUTE_SERVICE_SETTINGS'] = os.path.abspath('service/compute/settings.py')
app.config.from_envvar('COMPUTE_SERVICE_SETTINGS')
print(app.config)

api = Api(app)
api.add_resource(RootResource, RootResource.URI)
api.add_resource(TasksResource, TasksResource.URI)
api.add_resource(TaskResource, TaskResource.URI.format('<string:id>'))
api.add_resource(PipelinesResource, PipelinesResource.URI)

cache = SimpleCache()


# ----------------------------------------------------------------------------------------------------------------------
@api.representation('application/json')
def output_json(data, code, headers=None):
    response = make_response(json.dumps(data), code)
    response.headers.extend(headers or {})
    return response


# ----------------------------------------------------------------------------------------------------------------------
@app.before_request
def before_request():
    g.config = app.config
    g.cache = cache


if __name__ == '__main__':

    init_env()

    # Setup broker and result backend URLs
    os.environ['BROKER_URL'] = 'amqp://guest:guest@192.168.99.100:5672//'
    os.environ['CELERY_RESULT_BACKEND'] = 'redis://192.168.99.100:6379/0'

    host = os.getenv('COMPUTE_SERVICE_HOST')
    port = os.getenv('COMPUTE_SERVICE_PORT')
    port = int(port)

    app.run(host=host, port=port)
