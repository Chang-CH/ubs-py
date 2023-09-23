from flask import Blueprint, render_template, session, jsonify, request, make_response


@greedymonkey.route("/payload_crackme", methods=["GET"])
def getCommon():
    return send_file("payload_crackme")
