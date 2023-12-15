#import necessary libraies
from flask import Flask, render_template, request
import tensorflow 
import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

#load model
model =load_model("plant.h5")
print("@@ Model loaded")

def pred_cot_dieas(cott_plant):
    test_image = load_img(cott_plant, target_size=(150,150))#load image
    print("@@ Got Image for prediction")

    test_image = img_to_array(test_image)/255   #convert image to np array
    test_image = np.expand_dims(test_image, axis = 0)#change 3d to 4d
    
    result = model.predict(test_image).round(3)  #predict disease or not
    print("@@ Row result = ", result)
    
    pred = np.argmax(result)  #get index in max value
    
    if pred == 0:
        return "Healthy Plant", 'healthy.html'
    
    elif pred == 1:
        return "Powdery Plant", 'powdery.html'
    
    else:
        return "Rust Plant", 'rust.html'
    
#------------>>>pred_disease<<---end

#create flask instance

app = Flask(__name__)

#render index file
@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files["image"]
        filename = file.filename
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join("static//user uploaded//", filename)
        file.save(file_path)
        
        print("@@ Predicting class.......")
        pred, output_page = pred_cot_dieas(cott_plant=file_path)
        
        return render_template(output_page, pred_output = pred, user_image = file_path)

if __name__ == "__main__":
    app.run()
    






















    