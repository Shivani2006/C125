from flask import Flask, jsonify, request
from projectpred import getPrediction

app = Flask(__name__)

@app.route("/predict-alphabet", methods = ["POST"])
def predict():
    image = request.files.get("alphabet")
    result = getPrediction(image)
    return jsonify({"Prediction":result,"message":"done","status":"success"})

if __name__ == "__main__":
    app.run()