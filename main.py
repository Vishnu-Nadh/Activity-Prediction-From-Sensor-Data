from flask import Flask, json, request, jsonify, render_template, url_for
import os

app = Flask(__name__)
img_path = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = img_path


@app.route("/train", methods=["GET", "POST"])
def train():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data_dict = request.json
        print(data_dict)

        catogory = "testing"
        img = os.path.join(app.config["UPLOAD_FOLDER"] , "bending2.png")
        return render_template("result.html", catogory=catogory, img=img)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
