# AI Image Generation Studio

## Overview

AI Image Generation Studio is a Generative AI application built using Python and Gradio.

The project demonstrates:

- Text-to-Image Generation
- Image-to-Image Transformation
- Image Inpainting
- ControlNet Conditioning
- LoRA Training Interface

## Features

### Text-to-Image
Generate images from text prompts using Stable Diffusion concepts.

### Image-to-Image
Transform uploaded images using AI-based workflows.

### Inpainting
Modify selected regions of an image using prompts.

### ControlNet
Guide image generation using structural conditions.

### LoRA Training
Configure and train LoRA adapters for custom fine-tuning.

## Tech Stack

- Python
- Gradio
- Pillow
- OpenCV
- Hugging Face
- Google Colab
- Stable Diffusion

## Project Structure

AI-Image-Generation-Studio/
│
├── app.py
├── README.md
├── requirements.txt
│
├── assets/
├── outputs/
├── training/
│
└── src/
    ├── text_to_image.py
    ├── image_to_image.py
    ├── inpaint.py
    ├── controlnet.py
    └── lora_training.py

## Future Enhancements

- Stable Diffusion XL Integration
- Real ControlNet Models
- DreamBooth LoRA Training
- FastAPI Backend
- Hugging Face Deployment

## Author

Manikonda Saithriguna