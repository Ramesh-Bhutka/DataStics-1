# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import requests
import pickle
import io
import sklearn
from sklearn.preprocessing import StandardScaler
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model


# Loading crop recommendation model

car_price_prediction_model_path = 'models/Car-XGBregressor.pkl'
car_price_prediction_model = pickle.load(
    open(car_price_prediction_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations

# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/',methods=['GET'])
def home():
    title = 'D@taStics'
    return render_template('index.html', title=title)

@ app.route('/contact')
def contact():
    title = 'D@taStics'
    return render_template('contact.html', title=title)


@ app.route('/car-price-recommend')
def car_price_recommend():
    title = 'D@taStics'
    return render_template('car.html', title=title)


# ===============================================================================================


@ app.route('/car-price-predict', methods=['POST'])
def car_price_prediction():
    title = 'D@taStics'
    if  request.method=="POST":
        company = int(request.form['company'])
        kilometer_driven=float(request.form['kilometer_driven'])
        fuel_type=int(request.form['fuel_type'])
        transmission_type=int(request.form['transmission_type'])
        owner=int(request.form['owner'])
        engine_size=int(request.form['engine_size'])
        maxpower=int(request.form['maxpower'])
        seats=int(request.form['seats'])
        mileage=float(request.form['mileage'])
        year=int(request.form['year'])
        year=2020-year
        data = np.array([[company,kilometer_driven,fuel_type,transmission_type,owner,engine_size,maxpower,seats,mileage,year]])
    prediction=car_price_prediction_model.predict(data)
    #output=rou
    #return render_template("index.html",prediction_text="You Should grow {}".format(prediction))
    return render_template('car-result.html', prediction=prediction, title="D@taStics")


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
