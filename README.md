# 🖼️ Stable Diffusion: Text-to-Image Generation (Optimized for MPS)

This project **uses Stable Diffusion** to generate images from **text prompts**.  
It is optimized to run on **MPS (Apple Silicon GPUs)** to avoid **out-of-memory errors**.

---

## 🚀 Features
- **Generates images from text prompts** using **Stable Diffusion**.
- **Optimized for MPS (Apple Metal Performance Shaders)** on **Mac M1/M2**.
- **Lower memory usage** by reducing image size & inference steps.
- **Works on MPS, CUDA (Nvidia GPUs), or CPU** (with automatic detection).

---

## 📂 Project Structure
```
📁 project-folder
│── 📄 main.py          # Script to generate images
│── 📄 requirements.txt # Dependencies for Stable Diffusion
│── 📜 README.md        # This file (Instructions & setup guide)
```

---

## 🛠️ Installation & Setup

### ✅ **1. Clone the Repository**
```sh
git clone https://github.com/ganeshtati1209/Ganesh_intern_task2.git
cd YOUR_REPO_NAME
```

### ✅ **2. Create & Activate a Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### ✅ **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🎨 Generate Images from Text

To generate an image, **run the script**:
```sh
python main.py
```

### **Example Usage**
```
⚡ Using MPS (Apple Metal Performance Shaders) for faster execution.
Enter a text prompt: A snowy mountain at sunset
✅ Image saved as 'generated_image.png'
```
- The **generated image** will be displayed and saved as **`generated_image.png`**.

---

## 🛑 Troubleshooting

### **1️⃣ MPS Out of Memory?**
- Reduce image resolution in `main.py`:
  ```python
  height=320, width=320  # Reduce size
  ```

- Reduce inference steps:
  ```python
  num_inference_steps=15
  ```

### **2️⃣ Running on CPU instead of MPS?**
- Ensure PyTorch detects MPS:
  ```python
  torch.backends.mps.is_available()
  ```
  If `False`, try updating PyTorch:
  ```sh
  pip install --upgrade torch torchvision torchaudio
  ```

---

## 📜 License
This project is open-source under the **MIT License**.

---

## ⭐ Contributing
Feel free to **fork & contribute** by submitting a pull request!

---

## 🔗 References
- [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)
- [PyTorch MPS Support](https://pytorch.org/docs/stable/notes/mps.html)
