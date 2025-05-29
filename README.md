# Pneumonia_disease_detection_app
🧠 Pneumonia Diagnosis App
This project is a full-stack AI-powered web application for medical image analysis and diagnostics, built using Streamlit. It supports user login, image prediction, dashboard monitoring, and model training functionalities.

🚀 Features
🔐 User Authentication – Secure login system using credentials stored in users.json.

🖼️ Medical Image Prediction – Upload and analyze images via predict.py using pre-trained models.

📊 Dashboard – Visualize predictions, model performance, and logs with dashboard.py.

🧪 Model Training – Train or retrain ML models using the train.py module.

🛠️ Utilities – Common helper functions and services available in utils.py.

📁 Model Management – Trained models are stored and loaded from the models/ directory.

🧰 Dev Container Support – Preconfigured for development with .devcontainer.

📂 Project Structure
bash
Copy
Edit
.
├── .devcontainer/       # Development container configs
├── __pycache__/         # Cached Python bytecode
├── models/              # Trained models
├── app.py               # Main Streamlit app
├── dashboard.py         # Monitoring and analytics
├── login.py             # Handles user authentication
├── predict.py           # Handles prediction logic
├── train.py             # Model training logic
├── utils.py             # Utility functions
├── users.json           # Stores user credentials
├── requirements.txt     # Python dependencies
├── .streamlitruntime.txt # Streamlit runtime config (if needed)
├── .gitattributes       # Git settings
└── README.md            # Project documentation
🛠️ Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
