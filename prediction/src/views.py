"""
    prediction.src.views
    ~~~~~~~~~~~~~~~~~~~~

    Provides main api endpoints
"""
from flask import Blueprint, jsonify, request

from .algorithms import classify
from .algorithms import identify
from .algorithms import segment


blueprint = Blueprint('blueprint', __name__)


# The predict methods for each of the possible ML algorithms
PREDICTORS = {
    'classify': classify.trained_model.predict,
    'identify': identify.trained_model.predict,
    'segment': segment.trained_model.predict
}


@blueprint.route('/')
def home():
    """Shows the API info"""
    rkwargs = {
        'description': 'Shows API info',
        'message': 'Welcome to the lung cancer prediction API!',
        'links': {algo: '{}{}/predict/'.format(request.url_root, algo) for
                  algo in PREDICTORS.keys()}
    }

    return jsonify(**rkwargs)


@blueprint.route('/<algorithm>/predict/', methods=['GET', 'POST'])
def predict(algorithm):
    """Performs various predictions for a path to a DICOM directory (folder of
    scans).

    A GET request will give the documentation for the endpoint.

    A POST request with Content-Type set to "application/json" and the
    right parameters for the algorithm will call predict.

    All of the algorithms take a `dicom_path` parameter with a path to the
    file to perform the prediction on.

    Some algorithms also take:
        centroids (list[dict]): A list of centroids of the form::
            {'x': int,
             'y': int,
             'z': int}
    Args:
        algorithm (str): The prediction algorithm to use. One of 'segment',
            'classify', or 'identify'.
    """
    # empty string to track if there was an
    error = ''

    # dictionary to hold the response
    response = dict()

    if algorithm not in PREDICTORS:
        errormsg = 'Error! {} is not a valid algorithm. Please choose from {}.'
        error = errormsg.format(algorithm, set(PREDICTORS))

    # describe API on GET
    elif request.method == 'GET':
        response.update({
            'description': 'API documentation goes here.',
        })

    # make predictions on POST
    elif request.method == 'POST':

        payload = request.json

        try:
            predict_method = PREDICTORS[algorithm]

            if 'centroids' in payload:
                prediction = predict_method(payload['dicom_path'],
                                            payload['centroids'])
            else:
                prediction = predict_method(payload['dicom_path'])

            response.update({
                'prediction': prediction
            })

        except Exception:
            error = "There was an error with your request."

    # set the status code and messages for the response
    if error:
        response.update({
            'error': error,
            'status': 500
        })
    else:
        response.update({
            'status': 200,
        })

    resp = jsonify(**response)
    resp.status_code = response['status']
    return resp
