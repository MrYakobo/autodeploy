#!/usr/bin/python3

import os
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from glob import glob
import json
import subprocess

app = Flask(__name__, template_folder="")

with open("config.json") as f:
    config = json.load(f)


def deploy(js):
    if js["repository"]["name"] not in config:
        return "REPOSITORY NOT FOUND", 404

    p = config[js["repository"]["name"]]
    subprocess.run(["git", "pull"], cwd=p["path"])
    subprocess.run(["systemctl", "restart", p["service"]])


@app.route("/", methods=["POST", "GET"])
def idx():
    if request.method == "POST":
        return deploy(request.json)

    return str(list(config.keys()))


if __name__ == "__main__":
    app.run("0.0.0.0", port=int(os.getenv("PORT", 5000)))
