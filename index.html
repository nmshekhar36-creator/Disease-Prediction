from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load accuracy
try:
    with open("accuracy.txt", "r") as f:
        accuracy = float(f.read())
except:
    accuracy = 0.0


@app.route("/")
def home():
    return render_template("index.html", accuracy=accuracy)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form (Age, BP, Cholesterol, Sugar)
        values = [float(x) for x in request.form.values()]

        # Convert to numpy array
        input_data = np.array([values])

        # Prediction
        prediction = model.predict(input_data)

        print("Prediction:", prediction)

        # Result
        if prediction[0] == 0:
            result = "💚 No Disease"
        else:
            result = "❤️ Disease Detected"

        return render_template(
            "index.html",
            prediction_text=result,
            accuracy=accuracy
        )

    except Exception as e:
        print("Error:", e)
        return render_template(
            "index.html",
            prediction_text="Error in input data!",
            accuracy=accuracy
        )


if __name__ == "__main__":
    app.run(debug=True)