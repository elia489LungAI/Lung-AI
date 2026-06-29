import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

# Page Setup
st.set_page_config(page_title="AI Image Generator", layout="centered")
st.title("Lung AI - Image Generator 🎨")

# Load Model - Optimized to run on any device
@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    
    # Auto-detect device
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    
    # Load model with appropriate data type
    dtype = torch.float16 if device != "cpu" else torch.float32
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=dtype)
    return pipe.to(device)

# Initialize engine
with st.spinner("Initializing AI engine..."):
    pipe = load_model()

# Input
prompt = st.text_input("Enter your image description:")

# Generator Button
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Drawing... please wait"):
            # Image generation
            image = pipe(prompt).images[0]
            st.image(image, caption="Generated Image", use_container_width=True)
    else:
        st.warning("Please enter a prompt first.")