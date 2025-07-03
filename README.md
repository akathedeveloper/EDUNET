# 🗑️ Smart Waste Classification with Transfer Learning 🚀

**Status:** ✅ *Deployed*

A deep learning-powered system to automatically classify household waste into **six recyclable categories** using **state-of-the-art transfer learning** with advanced CNN backbones.  
This project benchmarks **EfficientNetV2** (S, M, B2, L), **EfficientNetB0**, **MobileNetV2**, and **ResNet50** — identifying the best model for real-world deployment.  
An interactive **Gradio** web app is hosted live on **Hugging Face Spaces** for anyone to test!

![image](https://github.com/user-attachments/assets/75cd0170-f7fe-4234-b748-0f1ce4ff170f)


---

## ♻️ Waste Categories

This classifier can recognize:

- 📦 **Cardboard**
- 🧪 **Glass**
- ⚙️ **Metal**
- 📄 **Paper**
- 🧴 **Plastic**
- 🚮 **Trash**

---

## 🌐 Live Demo

Try it instantly in your browser — no setup needed:  
👉 [**Launch the Gradio App on Hugging Face Spaces**](https://huggingface.co/spaces/akathedeveloper/Garbage-Classifier)  


---

## ✨ Highlights

- ✅ **Multiple CNN Backbones**: Benchmarks **EfficientNetV2S**, **EfficientNetV2M**, **EfficientNetV2B2**, **EfficientNetV2L**, **EfficientNetB0**, **MobileNetV2**, and **ResNet50**.
- 🔬 **Transfer Learning**: Leverages pretrained ImageNet weights for faster convergence and better generalization.
- ⚖️ **Class Imbalance Handling**: Uses computed class weights to balance the dataset effectively.
- 📊 **Clear Performance Metrics**: Visualizes training curves, final test accuracy, classification reports, and confusion matrix.
- 🏆 **Top Model**: **EfficientNetB0** achieved **91.97% test accuracy**, outperforming larger variants while remaining computationally efficient.
- ☁️ **Deployed on Hugging Face Spaces**: Zero local setup — fully serverless with **Gradio**.
- 🧩 **Modular Code**: Clean notebooks for data prep, training, evaluation, and deployment.
- 🖼️ **Sample Predictions**: Visualizations of real test images with predicted vs. true labels.

---

## 🔢 Final Results

| Model            | Test Accuracy |
|------------------|----------------|
| EfficientNetV2S  | 89.16%         |
| EfficientNetV2M  | 91.57%         |
| EfficientNetV2B2 | 88.76%         |
| EfficientNetV2L  | 91.57%         |
| EfficientNetB0   | 🏆 **91.97%**  |
| MobileNetV2      | 19.68%         |
| ResNet50         | 85.54%         |

**Conclusion:**  
EfficientNetB0 offers the best balance of accuracy and efficiency for this dataset — making it the ideal choice for real-world deployment.

---

## 📂 Project Structure Githup

```plaintext
├── notebooks/           # Jupyter Notebooks: training, evaluation, deployment
├── README.md            # This file
```
## 📂 Project Structure HuggingFace
```plaintext
├── models/              # Saved models (.keras)  
├── gradio_app.py        # Gradio inference script
├── requirements.txt     # Dependencies
