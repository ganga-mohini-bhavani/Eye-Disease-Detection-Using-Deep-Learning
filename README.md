# 👁️ EyeDiseaseDetect: Deep Learning-Based Classification of Eye Diseases

This project is developed as part of a SmartBridge-guided AI Fundamentals internship, focusing on applying deep learning techniques for healthcare. The system uses Transfer Learning with VGG19 to classify common eye diseases from retinal images, supporting early diagnosis and improving patient outcomes.

## 🚀 Features

- 🧠 **Transfer Learning** using VGG19 for accurate and efficient image classification  
- 👁️ **Detects Eye Conditions**: Cataract, Diabetic Retinopathy, Glaucoma, and Normal  
- 📷 Upload a retinal image and receive an instant diagnosis  
- 🌐 **Flask-based web app** with intuitive user interface  
- 📱 **Mobile-friendly** and responsive design  

## 🛠️ Technologies Used

- Python  
- TensorFlow & Keras  
- VGG19 (Transfer Learning)  
- Flask (Web Framework)  
- HTML, CSS, Bootstrap  
- Jupyter Notebook  
- Git & GitHub  

---

## 📁 Folder Structure

eye_disease_project/

├── app.py

├── evgg.h5 # Trained VGG19 model

├── static(uploaded images)

│ └── sample_eye.jpg

├── templates

│ ├── index.html

│ └── predict.html

├── eye_disease_dataset

│  └── cataract

│  └── diabetic_retinopathy

│  └── glaucoma

│  └── normal

📷 Sample Usage

- Train or load the model (evgg.h5)

Run the Flask app:

- python app.py

- Open your browser and go to http://127.0.0.1:5000

- Navigate to the prediction page and upload an retinal image

✅ The system will display the predicted eye condition — Cataract, Diabetic Retinopathy, Glaucoma, or Normal — instantly after uploading the image.

📌 Notes

- The dataset was sourced from the Eye Disease Detection dataset available on Kaggle

- This project demonstrates the power of transfer learning in medical imaging applications

