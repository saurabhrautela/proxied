import requests
from flask import Flask, request, render_template, flash
from requests.exceptions import ConnectionError
from form import UrlForm

app = Flask(__name__)
app.secret_key = r"D.[WBYn@=3d9fj2j$.J9V%Nh~ZMtd,MZmz)drfFeZ<Ff{m\XmVvLm7hY%"


@app.route("/", methods=["GET", "POST"])
def get_web_page():
    """Get home page of Arch Linux website."""
    form = UrlForm()

    if request.method == "POST":
        url = request.form["url"]

        try:
            response = requests.request("GET", url=url)
        except ConnectionError:
            flash("Not able to access the Internet.")
        except requests.exceptions.MissingSchema as e:
            flash(str(e.args))
        else:
            return render_template("index.html", form=form, website=response.text)

    return render_template("index.html", form=form)


@app.route("/allowed")
def get_list_of_allowed_websites():
    """Get list of all the websites the application is allowed to access."""
    with open("../tools/tinyproxy/filter", "r") as filter_file:
        websites = filter_file.read().split("\n")

    return str(websites[:-1])


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
