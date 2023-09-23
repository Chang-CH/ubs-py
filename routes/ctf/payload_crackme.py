from flask import Blueprint, render_template, session, jsonify, request, make_response, send_file

payload_crackme = Blueprint("payload_crackme", __name__)

@payload_crackme.route("/payload_crackme", methods=["GET"])
def getCommon():
    return send_file("payload_crackme")
