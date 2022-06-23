import json
import logging
import os
from argparse import ArgumentParser
from flask import Flask, Response, render_template
from gqlalchemy import Memgraph

log = logging.getLogger(__name__)

def init_log():
    logging.basicConfig(level=logging.DEBUG)
    log.info("Logging enabled")
    # Set the log level for werkzeug to WARNING because it will print out too much info otherwise
    logging.getLogger("werkzeug").setLevel(logging.WARNING)


def parse_args():
    #Parse command line arguments.
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="0.0.0.0", help="Host address.")
    parser.add_argument("--port", default=5000, type=int, help="App port.")
    parser.add_argument("--template-folder", default="public/template", help="Flask templates.")
    parser.add_argument("--static-folder", default="public", help="Flask static files.")
    parser.add_argument("--path-to-input-file", default="graph.cypherl", help="Graph input file.")
    parser.add_argument("--debug", default=True, action="store_true", help="Web server in debug mode.")
    print(__doc__)
    return parser.parse_args()

args = parse_args()


app = Flask(
    __name__,
    template_folder=args.template_folder,
    static_folder=args.static_folder,
    static_url_path="",
)


# Retrieve the home page for the app
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



# Entrypoint for the app that will be executed first
def main():
    # Code that should only be run once
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        init_log()
    app.run(host=args.host,
            port=args.port,
            debug=args.debug)

if __name__ == "__main__":
    main()

