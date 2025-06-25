# 🧠 Smart Waste Classification with EfficientNet & MobileNet

**Status:** 🚧 *In Progress*  
A deep learning-powered system for classifying waste into recyclable categories using both transfer learning and custom CNN layers. This project explores different architectures (EfficientNetV2 variants, MobileNet) to build an accurate and efficient garbage classifier.  
Includes an interactive web app built with **Streamlit** for real-time image classification.

---

## 🧾 Waste Categories
This model is trained to recognize and classify the following types of waste:

- 📦 **Cardboard**
- 🧪 **Glass**
- ⚙️ **Metal**
- 📄 **Paper**
- 🧴 **Plastic**
- 🚮 **Trash**

---

## 🌐 Live Web Demo
Test the model live without any local installation:

🔗 [Launch on Streamlit Cloud](#)  (In progress)

---

## ✨ Key Features

- **Multi-Model Framework**: Supports EfficientNetV2 (B0–B3), MobileNetV2, and custom CNNs for benchmarking and comparison.
- **Transfer Learning Integration**: Uses pretrained ImageNet weights for improved generalization and faster training.
- **Streamlit Web App**: Clean browser-based UI to upload images and get instant predictions.
- **Performance Visualization**: Plots for training accuracy, loss curves, and evaluation metrics.
- **Confusion Matrix & Reports**: Detailed analysis using precision, recall, and F1-score per class.
- **Modular Codebase**: Cleanly organized scripts for training, evaluation, prediction, and UI integration.
- **Model Persistence**: Save/load top-performing `.keras` models.
- **Data Augmentation**: Training pipeline includes real-time preprocessing and augmentation.

---

## 🧰 Tech Stack

- **TensorFlow/Keras** – Deep learning framework
- **EfficientNetV2 / MobileNetV2** – Transfer learning backbones
- **Custom CNN** – Custom-tailored classification layers
- **Streamlit** – For building the interactive web interface
- **scikit-learn** – Evaluation metrics and classification report
- **Matplotlib & Seaborn** – Visualizing model performance
- **Python 3.10** – Project language
- **NumPy & Pandas** – Data preprocessing and manipulation
- **Jupyter Notebook** – Experimentation and visualization

---

## 📈 Model Evaluation

Evaluation outputs include:

- Accuracy and loss metrics across training epochs
- Confusion matrix on the test set
- Per-class metrics (precision, recall, F1-score)

---

## 🧩 Architecture Overview

The training pipeline:

1. **Feature Extractor**: EfficientNetV2 or MobileNet with frozen base layers
2. **Custom Head**: Convolutional layers fine-tuned for the waste domain
3. **Fine-Tuning Phase**: Unfreezing selected layers for improved performance
4. **Evaluation**: Performance metrics, confusion matrix, and sample predictions

---

## 🖼 Sample Predictions

Sample outputs demonstrate accurate classification across all six waste categories. Misclassifications are rare and mostly occur between visually similar items (e.g., metal vs glass).

---

## 🧪 Getting Started

```bash
git clone https://github.com/your-username/smart-waste-classification.git
cd smart-waste-classification
pip install -r requirements.txt
streamlit run app.py  # Launch the Streamlit app
