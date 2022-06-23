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
