# PicTalk

This project is a Streamlit application that generates text descriptions from images and converts the generated text to speech using the `gTTS` library.

## Features

- Upload an image file (JPG, JPEG, PNG).
- Generate a text description of the uploaded image using the DistilGPT-2 model.
- Generate additional text from the description using the BLIP model.
- Convert the generated text to speech and play the audio.

## Installation

1. **Clone the repository:**

```sh
git clone https://github.com/Prajjval78/PicTalk.git
cd PicTalk
```

2. **Run the Streamlit application:**
```sh
streamlit run app.py
```

3. **Open your web browser and go to:**
```sh
http://localhost:8501
```
