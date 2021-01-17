import json
from flask import Response, request, redirect, render_template
from flask_restful import Resource

from app.controllers.emails import save_emails

class EmailResource(Resource):
    def post(self) -> Response:
        data = request.form
        status, result = save_emails(data)
        return Response(
            response=json.dumps(result), status=status, mimetype="application/json"
        )
