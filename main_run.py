import streamlit as st


st.header("Display Image")
image_path = "./media/pexels-enginakyurt-1435852.jpg"
with open(image_path, 'r+b') as image_f:
    image_bytes = image_f.read()
st.image(image_bytes,caption="a bird")

st.header("Display Video")
video_path = "./media/12217946_3840_2160_30fps.mp4"
with open(video_path, 'r+b') as video_f:
    video_bytes = video_f.read()
st.video(video_bytes)

st.header("Display Audio")
audio_path = "./media/tell-me-the-truth-260010.mp3"
with open(audio_path, 'r+b') as audio_f:
    audio_bytes = audio_f.read()
st.audio(audio_bytes)

