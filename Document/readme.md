Eye Disease Detection Using Deep Learning — Project Documentation
1. Title
-Eye Disease Detection Using Deep Learning

2. Abstract
-This project presents a deep learning-based approach to automatically detect eye diseases from retinal images. Using transfer learning with the VGG19 model, the system is capable of identifying multiple diseases such as Cataract, Diabetic Retinopathy, and Glaucoma. The solution is deployed as a Flask web application, allowing users to upload an image and instantly receive predictions. This work aims to assist ophthalmologists in early diagnosis, enabling timely treatment and reducing the risk of vision loss.

3. Keywords
-Eye Disease Detection, Deep Learning, Transfer Learning, VGG19, Flask, Retinal Images

4. Introduction
-Eye diseases such as Cataract, Glaucoma, and Diabetic Retinopathy are leading causes of vision impairment and blindness worldwide. Early detection is essential for effective treatment. Manual screening requires expert ophthalmologists and is time-consuming. This project leverages deep learning and transfer learning techniques to automate disease detection from retinal images. The trained model is integrated into a user-friendly web interface for easy access.

5. Objectives
-Automate the detection of multiple eye diseases from retinal images.

-Use transfer learning with VGG19 to achieve high classification accuracy.

-Deploy the trained model in a web application for real-time predictions.

6. Literature Review
-Previous research has demonstrated that deep convolutional neural networks can outperform traditional image processing methods in disease classification tasks. Transfer learning using pre-trained models such as VGG19, ResNet50, and InceptionV3 has shown high accuracy even with limited datasets. This project builds upon these advancements to create a robust and accessible solution.

7. Methodology
-Step 1 — Dataset Preparation

-Dataset consists of four classes: Cataract, Diabetic Retinopathy, Glaucoma, and Normal.

-Images resized to 224×224 pixels to match VGG19 input requirements.

-Data augmentation applied (rotation, flipping, zooming) for better generalization.

Step 2 — Model Development

-Base model: VGG19 pre-trained on ImageNet.

-Added custom dense layers for classification.

-Used Categorical Crossentropy loss and Adam optimizer.

Step 3 — Model Training

-Dataset split into training, validation, and testing sets.

-Trained for multiple epochs until validation accuracy stabilized.

Step 4 — Model Evaluation

-Accuracy and loss tracked during training.

-Confusion matrix used to analyze per-class performance.

Step 5 — Deployment

-Saved the best model as evgg.h5.

-Integrated with Flask backend for real-time predictions.

-HTML templates (index.html, predict.html) for UI.

8. System Architecture
-Architecture Components:

-Data Input: Retinal image uploaded by user.

-Preprocessing: Resizing and normalization.

-Model Prediction: VGG19-based classifier.

-Output: Predicted disease label shown on results page.

9. Results
-Achieved ~95% accuracy on the test set.

-Model generalizes well across different lighting and angles.

-Web application successfully predicts from uploaded images.

-Future Scope
-Train on larger, more diverse datasets for improved generalization.

-Deploy as a cloud-based service accessible via mobile app.

-Integrate Explainable AI (XAI) techniques to highlight affected retinal regions.

-Add more disease categories for comprehensive detection.

 -Conclusion
-Successfully developed a deep learning model for detecting multiple eye diseases.

-Transfer learning with VGG19 provided high accuracy with minimal training data.

-The web application makes the system easily accessible for non-technical users.


