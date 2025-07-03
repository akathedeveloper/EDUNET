import numpy as np
import tensorflow as tf
import gradio as gr

# Load your trained model
best_model = tf.keras.models.load_model("best_EffiB0.keras")

# Define your class names
class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
num_classes = len(class_names)

IMAGE_SIZE = (124, 124)  #

def classify_image(img):
    img = tf.image.resize(img, IMAGE_SIZE)[None, ...]
    preds = best_model.predict(img)
    return {class_names[i]: float(preds[0, i]) for i in range(num_classes)}


custom_footer = """
<p style="text-align: center;">
  Developed with ❤️ by <strong>Adhiraj</strong>
</p>
<p style="text-align: center;">
  <a href="https://www.linkedin.com/in/akathedeveloper/" target="_blank" style="display: inline-block; margin: 0 10px;">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
  </a>
  <a href="https://github.com/akathedeveloper" target="_blank" style="display: inline-block; margin: 0 10px;">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="30">
  </a>
</p>
"""

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Label(num_top_classes=3),
    title="Garbage Classifier",
    description="Classify images into cardboard, glass, metal, paper, plastic, or trash.",
    article=custom_footer
)

demo.launch()
