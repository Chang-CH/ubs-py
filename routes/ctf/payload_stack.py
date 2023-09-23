from flask import Blueprint, render_template, session, jsonify, request, make_response, send_file

payload_stack = Blueprint("payload_stack", __name__)

@payload_stack.route("/payload_stack", methods=["GET"])
def getCommon():
    return send_file("payload_stack")
