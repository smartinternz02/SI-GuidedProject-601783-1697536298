from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("Diabetes-Prediction.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        
        HighBP = int(request.form.get("HighBP") == "yes")
        HighChol = int(request.form.get("HighChol") == "yes")
        CholCheck = int(request.form.get("CholCheck") == "yes")
        BMI = float(request.form['BMI'])
        Smoker = int(request.form.get("Smoker") == "yes")
        Stroke = int(request.form.get("Stroke") == "yes")
        HeartDiseaseorAttack = int(request.form.get("HeartDiseaseorAttack") == "yes")
        PhysActivity = int(request.form.get("PhysActivity") == "yes")
        Fruits = int(request.form.get("Fruits") == "yes")
        Veggies = int(request.form.get("Veggies") == "yes")
        AnyHealthcare = int(request.form.get("AnyHealthcare") == "yes")
        NoDocbcCost = int(request.form.get("NoDocbcCost") == "yes")
        GenHlth = float(request.form['GenHlth'])
        MentHlth = float(request.form['MentHlth'])
        PhysHlth = float(request.form['PhysHlth'])
        DiffWalk = int(request.form.get("DiffWalk") == "yes")
        Sex = int(request.form.get("Sex") == "male")
        Age = float(request.form['Age'])
        Education = float(request.form['Education'])
        Income = float(request.form['Income'])
        hvyAlcoholConsump = int(request.form.get("hvyAlcoholConsump") == "yes")

        attributes = [
            HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack,
            PhysActivity, Fruits, Veggies, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth,
            PhysHlth, DiffWalk, Sex, Age, Education, Income, hvyAlcoholConsump
        ]

        attributes = [float(attr) for attr in attributes]
        pred = model.predict([attributes])
        index = ['No Diabetes', 'Pre Diabetes', 'Diabetes']
        result = "The Diabetes Prediction for this person is: " + index[pred[0]]
        return result  

if __name__=='__main__':
    app.run(debug=True) 