# 🌿 Plant Disease Detection using CNN (TensorFlow/Keras)

## 📌 Overview

This project is a **Convolutional Neural Network (CNN)** based image classification model built using **TensorFlow and Keras**. It is designed to classify plant leaf images into different disease categories using deep learning.

The model is trained on a dataset of plant leaf images organized into training, validation, and test folders.

---

## 🧠 Model Description

- **Model Type:** Convolutional Neural Network (CNN)  
- **Framework:** TensorFlow / Keras  
- **Input Image Size:** 150 x 150 pixels  
- **Output:** Multi-class classification (plant disease categories)  
- **Activation Functions:** ReLU (hidden layers), Softmax (output layer)  
- **Loss Function:** Categorical Crossentropy  
- **Optimizer:** Adam  

---

## 📁 Dataset Structure
dataset/
│
├── Train/
│ ├── Class_1/
│ ├── Class_2/
│ └── Class_3/
│
├── Validation/
│ ├── Class_1/
│ ├── Class_2/
│ └── Class_3/
│
└── Test/
├── Class_1/
├── Class_2/
└── Class_3/



---

## ⚙️ Workflow

1. Load dataset from directory structure  
2. Visualize sample images from each class  
3. Normalize images using `ImageDataGenerator`  
4. Build CNN model using Keras Sequential API  
5. Train model on training dataset  
6. Validate model on validation dataset  
7. Evaluate performance on test dataset  
8. Make predictions on new images  

---

## 🏗️ Model Architecture

- Conv2D (32 filters) + MaxPooling  
- Conv2D (64 filters) + MaxPooling  
- Flatten layer  
- Dense (128 units) + Dropout (0.25)  
- Dense (128 units) + Dropout (0.25)  
- Dense (128 units)  
- Dense (Softmax output layer)  

---

## 📊 Training Details

- Image size: 150x150  
- Batch size: 32  
- Epochs: 10 (with Early Stopping)  
- Data preprocessing: Rescaling (1./255)  
- Validation: Separate validation directory used  

---

## 📈 Evaluation

- Model evaluated on test dataset  
- Training and validation accuracy/loss plotted  
- Predictions visualized on sample test images  

---

## 🔍 Prediction

A custom function is used to:
- Load a test image  
- Preprocess it  
- Predict its class using the trained model  
- Display image with predicted label  

---

## 💻 Tech Stack

- Python  
- TensorFlow  
- Keras  
- NumPy  
- Matplotlib  
- OpenCV (for preprocessing ideas)  

---

## 🚀 Future Improvements

- Use Transfer Learning (MobileNet, ResNet, etc.)  
- Add data augmentation techniques  
- Improve model generalization  
- Add Confusion Matrix & Classification Report  
- Deploy using Streamlit / Flask  
- Convert into production-ready API  

---

## 👨‍💻 Author

**Pooja Bhavsar**  
Machine Learning Enthusiast | Deep Learning Projects
