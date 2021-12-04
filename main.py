from flask import Flask, json, request, jsonify, render_template, url_for
import os
from createDataset import Create_Dataset
from preprocessing import Preprocessor
from training import Train_Model

app = Flask(__name__)
img_path = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = img_path


@app.route("/train", methods=["GET", "POST"])
def train():
    if request.method == "POST":
        if request.json["key"] == "start":
            create_data = Create_Dataset("RawData")
            data = create_data.getAllData()
            preprocess = Preprocessor(data)
            X, Y = preprocess.Preprocess()
            train = Train_Model(X, Y)
            message = train.trainModel()
        return jsonify(message)
    else:
        return "post request expected !"


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data_dict = request.json
        print(data_dict)

        catogory = "testing"
        img = os.path.join(app.config["UPLOAD_FOLDER"], "bending2.png")
        return render_template("result.html", catogory=catogory, img=img)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
