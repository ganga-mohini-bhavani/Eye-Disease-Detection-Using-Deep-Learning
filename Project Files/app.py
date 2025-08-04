import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the trained eye disease detection model
model = load_model('evgg.h5')  # Ensure this file exists in the same directory or provide correct path

# Class labels (update if your dataset had different class names)
labels = ['Cataract', 'Diabetic Retinopathy', 'Glaucoma', 'Normal']

# Set up Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Upload page
@app.route('/upload')
def upload_page():
    return render_template('predict.html')

# Handle prediction after image is uploaded
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        # Load and preprocess image
        img = load_img(filepath, target_size=(224, 224))
        x = img_to_array(img) / 255.0
        x = np.expand_dims(x, axis=0)

        # Predict using the loaded model
        preds = model.predict(x, verbose=0)
        pred_class = labels[np.argmax(preds)]

        return render_template('predict.html', prediction=pred_class, image_path=filepath)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
