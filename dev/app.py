import requests
from flask import Flask
from requests.exceptions import ConnectionError

app = Flask(__name__)


@app.route("/")
def get_arch_linux_homepage():
    try:
        response = requests.request("GET", url="https://archlinux.org/")
    except ConnectionError:
        return "Not able to access the Internet.", 504
    return response.text


@app.route("/restricted")
def get_facebook_homepage():
    try:
        response = requests.request("GET", url="https://facebook.com")
    except ConnectionError:
        return "Not able to access the restricted URL.", 504
    return response.text


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
