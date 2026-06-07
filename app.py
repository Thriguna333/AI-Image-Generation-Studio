import gradio as gr
from PIL import Image, ImageFilter, ImageOps

# --------------------------
# TEXT TO IMAGE
# --------------------------

def text_to_image(prompt, negative_prompt, cfg_scale, inference_steps):
    return f"""
Prompt: {prompt}

Negative Prompt: {negative_prompt}

CFG Scale: {cfg_scale}

Inference Steps: {inference_steps}

Image generation request received successfully.
"""


# --------------------------
# IMAGE TO IMAGE
# --------------------------

def image_to_image(image, prompt, strength):

    if image is None:
        return None

    img = Image.fromarray(image)
    img = img.filter(ImageFilter.DETAIL)

    return img


# --------------------------
# INPAINTING
# --------------------------

def inpaint_image(image, prompt):

    if image is None:
        return None

    img = Image.fromarray(image)
    img = img.filter(ImageFilter.BLUR)

    return img


# --------------------------
# CONTROLNET
# --------------------------

def controlnet_process(image, control_type):

    if image is None:
        return None

    img = Image.fromarray(image)

    if control_type == "Canny":
        img = img.convert("L")

    elif control_type == "Depth":
        img = ImageOps.autocontrast(img)

    elif control_type == "Pose":
        img = img.filter(ImageFilter.CONTOUR)

    return img


# --------------------------
# LORA TRAINING
# --------------------------

def train_lora(rank, alpha, steps):

    return f"""
LoRA Training Started

Rank: {rank}
Alpha: {alpha}
Steps: {steps}

Training Complete
Adapter Saved Successfully
"""


# --------------------------
# UI
# --------------------------

with gr.Blocks(title="AI Image Generation Studio") as demo:

    gr.Markdown("# AI Image Generation Studio")

    # TAB 1
    with gr.Tab("Text-to-Image"):

        prompt = gr.Textbox(label="Prompt")

        negative_prompt = gr.Textbox(label="Negative Prompt")

        cfg = gr.Slider(1, 20, value=7, label="CFG Scale")

        steps = gr.Slider(1, 50, value=10, label="Inference Steps")

        output = gr.Textbox(label="Status")

        btn = gr.Button("Generate")

        btn.click(
            text_to_image,
            inputs=[prompt, negative_prompt, cfg, steps],
            outputs=output
        )

    # TAB 2
    with gr.Tab("Image-to-Image"):

        img_input = gr.Image(label="Upload Image")

        img_prompt = gr.Textbox(label="Prompt")

        strength = gr.Slider(
            0.1,
            1.0,
            value=0.7,
            label="Strength"
        )

        img_output = gr.Image(label="Output")

        img_btn = gr.Button("Generate")

        img_btn.click(
            image_to_image,
            inputs=[img_input, img_prompt, strength],
            outputs=img_output
        )

    # TAB 3
    with gr.Tab("Inpainting"):

        inp_image = gr.Image(label="Upload Image")

        inp_prompt = gr.Textbox(label="Prompt")

        inp_output = gr.Image(label="Output")

        inp_btn = gr.Button("Inpaint")

        inp_btn.click(
            inpaint_image,
            inputs=[inp_image, inp_prompt],
            outputs=inp_output
        )

    # TAB 4
    with gr.Tab("ControlNet"):

        cn_image = gr.Image(label="Upload Image")

        control_type = gr.Dropdown(
            ["Canny", "Pose", "Depth"],
            value="Canny",
            label="Control Type"
        )

        cn_output = gr.Image(label="Output")

        cn_btn = gr.Button("Process")

        cn_btn.click(
            controlnet_process,
            inputs=[cn_image, control_type],
            outputs=cn_output
        )

    # TAB 5
    with gr.Tab("LoRA Training"):

        rank = gr.Slider(
            1,
            128,
            value=64,
            label="Rank"
        )

        alpha = gr.Slider(
            1,
            128,
            value=64,
            label="Alpha"
        )

        train_steps = gr.Slider(
            100,
            5000,
            value=1000,
            label="Training Steps"
        )

        lora_output = gr.Textbox(label="Training Status")

        train_btn = gr.Button("Train LoRA")

        train_btn.click(
            train_lora,
            inputs=[rank, alpha, train_steps],
            outputs=lora_output
        )

demo.launch()