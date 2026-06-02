from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('data_lupus_model.pkl')


# Login page
@app.route('/')
def home():
    return render_template('login.html')


# Login
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "admin123":
        return render_template('predict.html')

    return "Invalid Username or Password"


# Prediction
@app.route('/predict', methods=['POST'])
def predict():

    Age = float(request.form['Age'])
    Gender = float(request.form['Gender'])
    Sickness = float(request.form['Sickness'])
    Esbach = float(request.form['Esbach'])
    MBL = float(request.form['MBL'])
    ESR = float(request.form['ESR'])
    C3 = float(request.form['C3'])
    C4 = float(request.form['C4'])
    CRP = float(request.form['CRP'])
    ANA = float(request.form['ANA'])
    ANTIdsDNA = float(request.form['ANTIdsDNA'])
    SLEDAI = float(request.form['SLEDAI'])

    data = np.array([[Age,
                      Gender,
                      Sickness,
                      Esbach,
                      MBL,
                      ESR,
                      C3,
                      C4,
                      CRP,
                      ANA,
                      ANTIdsDNA,
                      SLEDAI]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Patient Has Lupus"
    else:
        result = "Patient Does Not Have Lupus"

    return render_template(
        'result.html',
        prediction_text=result
    )


if __name__ == "__main__":
    app.run(debug=True)