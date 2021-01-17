import json
from flask import Response, request, redirect, render_template
from flask_restful import Resource

from app.controllers.emails import save_emails, save_recipients

class EmailResource(Resource):
    def post(self) -> Response:
        data = request.json
        status, result = save_emails(data)
        return Response(
            response=json.dumps(result), status=status, mimetype="application/json"
        )


class RecipientResource(Resource):
    def post(self) -> Response:
        data = request.json
        status, result = save_recipients(data)
        return Response(
            response=json.dumps(result), status=status, mimetype="application/json"
        )
