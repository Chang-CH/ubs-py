from flask import Blueprint, render_template, session, jsonify, request, make_response, send_file

payload_shellcode = Blueprint("payload_shellcode", __name__)

@payload_shellcode.route("/payload_shellcode", methods=["GET"])
def getCommon():
    return send_file("payload_shellcode")
