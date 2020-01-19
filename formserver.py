import datetime

import flask

app = flask.Flask(__name__)


@app.route("/contact", methods=["POST"])
def contact():
    form = flask.request.form
    header = f"Form submission received at {datetime.datetime.now():%H:%M:%S}"
    output = f"""
{header}
{len(header) * '-'}
name: {form['name']}
email: {form['email']}
message: {form['message']}

    """
    print(output)
    return "", 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
