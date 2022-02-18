from flask import Flask, json, request, jsonify, render_template, url_for
import os
import pandas as pd
from createDataset import Create_Dataset
from preprocessing import Preprocessor
from training import Train_Model
from prediction import Predict_Output

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
        if request.form:
            feilds = [
                "avg_rss12",
                "var_rss12",
                "avg_rss13",
                "var_rss13",
                "avg_rss23",
                "var_rss23",
            ]
            data_dict = {}
            for item in feilds:
                data_dict[item] = [float(request.form[item])]

            data = pd.DataFrame(data_dict)
            preprocess = Preprocessor(data)
            df = preprocess.preprocessPred()
            predict = Predict_Output(df)
            output = predict.preditOutput()

            catogory = output
            if catogory == "bending2":
                image_name = catogory + ".png"
            else:
                image_name = catogory + ".svg"

            img = os.path.join(app.config["UPLOAD_FOLDER"], image_name)

            return render_template("result.html", catogory=catogory, img=img)
        else:
            return "error in sending form data"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
