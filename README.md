# 🧠 Smart Waste Classification with EfficientNet & MobileNet

**Status:** 🚧 *In Progress*  
A deep learning-powered system for classifying waste into recyclable categories using both transfer learning and custom CNN layers. This project explores different architectures (EfficientNetV2 variants, MobileNet) to build an accurate and efficient garbage classifier. 
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
Test the model live without downloading anything:

🔗 [Launch on Hugging Face Spaces](#)

---

## ✨ Key Features

- **Multi-Model Framework**: Supports EfficientNetV2 (B0–B3), MobileNetV2, and custom CNNs for benchmarking and comparison.
- **Transfer Learning Integration**: Leverages pretrained ImageNet weights for better generalization and faster training.
- **Interactive Gradio UI**: Use webcam or image upload directly in the browser for predictions.
- **Performance Visualization**: Graphs showing accuracy, loss, and training trends.
- **Confusion Matrix & Reports**: Evaluate model precision, recall, and F1-score per class.
- **Modular Codebase**: Clearly separated scripts for training, evaluation, and deployment.
- **Model Saving & Loading**: Store best `.keras` models and reload for inference instantly.
- **Augmented Data Pipeline**: Robust training pipeline with real-time image augmentation.

---

## 🧰 Tech Stack

- **TensorFlow/Keras** – Core deep learning framework
- **EfficientNetV2 / MobileNetV2** – Transfer learning models
- **Custom CNN** – For experimentation and flexibility
- **Gradio** – For building browser-based UIs
- **scikit-learn** – Evaluation metrics and classification reports
- **Matplotlib & Seaborn** – For training curves and result visualization
- **Python 3.10** – Main programming language
- **NumPy & Pandas** – Data handling and preprocessing
- **Jupyter Notebook** – For prototyping and model development

---

## 📈 Model Evaluation

Includes:

- Accuracy/Loss progression across epochs
- Confusion matrix for visual error analysis
- Detailed per-class classification reports (precision, recall, F1-score)

---

## 🧩 Architecture Overview

The model follows this training pipeline:

1. **Base Feature Extractor**: EfficientNetV2 or MobileNet with frozen layers
2. **Custom CNN Head**: Domain-specific layers for waste classification
3. **Fine-Tuning**: Unfreeze base layers and optimize end-to-end
4. **Evaluation**: Metrics, graphs, confusion matrix, and test predictions

---

## 🖼 Sample Predictions

Example predictions from the test set show high confidence and accuracy across all classes. Misclassifications are rare and typically occur between visually similar categories (e.g., metal vs glass).

---

## 🧪 Getting Started

```bash
git clone https://github.com/your-username/smart-waste-classification.git
cd smart-waste-classification
pip install -r requirements.txt
python app.py  # Launch Gradio interface
