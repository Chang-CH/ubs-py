from flask import Flask
from routes.challenge1.lazydev import lazydev
from routes.challenge2.greedymonkey import greedymonkey
from routes.ctf.payload_crackme import payload_crackme
from routes.ctf.payload_stack import payload_stack
from routes.ctf.payload_shellcode import payload_shellcode
from routes.chess.minichess import minichess
from routes.maze.maze import maze

import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/", methods=["GET"])
def default_route():
    return "Python Template"


app.register_blueprint(lazydev)
app.register_blueprint(greedymonkey)
app.register_blueprint(payload_crackme)
app.register_blueprint(payload_stack)
app.register_blueprint(payload_shellcode)
app.register_blueprint(minichess)
app.register_blueprint(maze)

# logger = logging.getLogger()
# handler = logging.StreamHandler()
# formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)

# if __name__ == "__main__":
#     logging.info("Starting application ...")
#     app.run(port=8080, debug=True)
