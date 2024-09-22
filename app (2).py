import streamlit as st
from PIL import Image as PilImage
from transformers import BlipProcessor, BlipForConditionalGeneration, AutoModelForCausalLM, AutoTokenizer
from gtts import gTTS

# Load the BLIP processor and model for image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load the DistilGPT-2 model and tokenizer
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate a description from an image
def generate_description(image):
    inputs = blip_processor(image, return_tensors="pt")
    caption_ids = blip_model.generate(**inputs)
    description = blip_processor.decode(caption_ids[0], skip_special_tokens=True)
    return description

# Function to generate text from a description
def generate_text_from_description(description):
    input_ids = tokenizer(description, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=50)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Function to convert text to speech using gTTS
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    return "speech.mp3"

# Streamlit interface
st.title("Image to Text Generator and Text to Speech")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = PilImage.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Generating description...")
    
    description = generate_description(image)
    st.write("Generated Description:", description)
    
    st.write("Generating text from description...")
    generated_text = generate_text_from_description(description)
    st.write("Generated Text:", generated_text)
    
    st.write("Converting text to speech...")
    audio_file = text_to_speech(generated_text)
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')