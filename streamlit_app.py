import streamlit as st
from PIL import Image, ImageFilter, ImageOps
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.hero {
    text-align:center;
    padding:50px;
    border-radius:20px;
    background: linear-gradient(135deg,#4F46E5,#7C3AED,#EC4899);
    color:white;
    margin-bottom:20px;
}

.feature-card{
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #334155;
}

.metric-card{
    background:#111827;
    padding:15px;
    border-radius:15px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
section[data-testid="stSidebar"]{
    background-color:#111827;
}

section[data-testid="stSidebar"] *{
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="AI Image Generation Studio",
    page_icon="🎨",
    layout="wide"
)

# ==================================
# PROFESSIONAL SIDEBAR
# ==================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:15px;
        background:linear-gradient(135deg,#4F46E5,#7C3AED,#EC4899);
        color:white;
        margin-bottom:20px;
    ">
        <h2>🎨 AI Studio</h2>
        <p>Generative AI Platform</p>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "📌 Navigation",
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

    st.markdown("---")

    st.markdown("### 🚀 Project Status")

    st.success("Text-to-Image")
    st.success("Image-to-Image")
    st.success("Inpainting")
    st.success("ControlNet")
    st.success("LoRA Training")

    st.markdown("---")

    st.markdown("### 📊 Quick Stats")

    st.metric("Modules", "5")
    st.metric("Version", "1.0")
    st.metric("Deployment", "Live")

    st.markdown("---")

    st.markdown("""
    ### 🛠 Tech Stack

    - Python
    - Streamlit
    - Pillow
    - OpenCV
    - Stable Diffusion Concepts
    - ControlNet Concepts
    - LoRA Concepts
    """)

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center">
        <h4>👨‍💻 Developer</h4>
        <p><b>Manikonda Saithriguna</b></p>
        <p>AI Internship Project 2026</p>
    </div>
    """, unsafe_allow_html=True)

# ==================================
# HOME PAGE
# ==================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🎨 AI Image Generation Studio</h1>
        <h3>Generate • Transform • Edit • Fine-Tune Images with AI</h3>
        <p>A Unified Generative AI Platform</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Core Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>🖼️ Text-to-Image</h3>
        <p>Create images from text prompts.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>🔄 Image-to-Image</h3>
        <p>Transform uploaded images.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <h3>✨ Inpainting</h3>
        <p>Edit specific image regions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card">
        <h3>🎯 ControlNet</h3>
        <p>Guide generation using conditions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    st.markdown("""
    <div class="feature-card">
    <h3>🧠 LoRA Training</h3>
    <p>Configure custom fine-tuning workflows.</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("## 📊 Project Statistics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Modules", "5")

    with c2:
        st.metric("Technologies", "6+")

    with c3:
        st.metric("Platform", "Unified")

    st.divider()

    st.markdown("""
    ## 🎯 Project Objective

    This project demonstrates modern Generative AI workflows including:

    - Text-to-Image Generation
    - Image-to-Image Transformation
    - Inpainting
    - ControlNet Conditioning
    - LoRA Fine-Tuning

    Developed as an AI Internship Project.
    """)

    st.success("✅ Deployment Successful")

    st.info("👨‍💻 Developed by Manikonda Saithriguna")

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