from flask import Flask, render_template, request
import pandas as pd
import pickle
app=Flask(__name__)
data=pd.read_csv("cleaned_data.csv")
pipe=pickle.load(open("RidgeModel.pkl","rb"))

@app.route("/")
def index():
    locations=sorted(data["location"].unique())
    return render_template("index.html",locations=locations)

@app.route('/predict', methods=['POST'])
def predict():

    sqft = float(request.form['sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']
    balcony = request.form['balcony']

    input=pd.DataFrame([[location,sqft,bath,balcony,bhk]],columns=["location","total_sqft","bath","balcony","bhk"])
    prediction= pipe.predict(input)[0]

    return render_template(
        'index.html',
        prediction_text=f"Estimated Price: ₹ {prediction:.2f} Lakhs")


if __name__=="__main__":
    app.run(debug=True,port=5001)
