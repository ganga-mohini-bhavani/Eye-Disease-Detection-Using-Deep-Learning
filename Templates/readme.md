🧾 HTML Templates (Flask Frontend)
The templates folder contains the frontend pages rendered by Flask for user interaction. These templates are written in HTML and styled with Bootstrap to provide a modern and responsive UI for users.

📄 index.html
This is the landing page of the application.

Features a welcome message and a "Get Started" button that routes the user to the prediction interface.

Provides a clean and user-friendly introduction to the project purpose.

🔹 Rendered At: http://127.0.0.1:5000/
🔹 Routed By: @app.route('/') in app.py

📄 predict.html
The main interaction page for users to:

Upload retina images

Trigger disease prediction

View the uploaded image alongside the predicted class (e.g., Cataract, Glaucoma)

🔹Displays both:

✅ The prediction result

🖼️ The uploaded image (from /static/)

🔹 Rendered At: http://127.0.0.1:5000/upload and /predict
🔹 Routed By: @app.route('/upload') and @app.route('/predict', methods=['POST'])
