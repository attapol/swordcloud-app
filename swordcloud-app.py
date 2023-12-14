"""Streamlit app that creates word clouds from text files or text box input.

The app uses swordcloud library to create word clouds from text files or text
box input.
"""

import streamlit as st
import swordcloud
from swordcloud.color_func import SingleColorFunc, FrequencyColorFunc
from utils import detect_lang

# Set page title
st.set_page_config(page_title="Swordcloud", page_icon="🗡️", layout='wide')

# Set title
st.title("Semantic word cloud")

# # Text box input
st.markdown("Create a semantic word cloud from Thai or English text.")
text = st.text_area("Enter text in the text box below to create a word cloud.", height=250)

# # Upload text file input
# st.header("Or upload a text file input")
# st.markdown("Upload a text file to create a word cloud.")
# uploaded_file = st.file_uploader("Choose a file")
# two columns layout
col1, col2 = st.columns(2)
# Show text box input and upload text file input side by side
with col1:
    st.subheader("Or upload a text file input")
    st.markdown("Upload a text file to create a word cloud.")
    generate_button = st.button("Generate")
with col2:
    uploaded_file = st.file_uploader("Choose a file")


# Create word cloud when hit "Generate" button
if generate_button:
    # If both text area and upload file are not filled, show error message
    if text and uploaded_file:
        st.error("Please enter either text or a text file.")
        st.stop()

    # If text area is filled, use text area input
    if text:
        text_input = text
    else:
        text_input = uploaded_file.read().decode("utf-8")

    lang = detect_lang(text_input)
    wc = swordcloud.SemanticWordCloud(language=lang,
        width = 1600,
        height = 800,
        max_font_size = 150,
        prefer_horizontal = 1,
        color_func = SingleColorFunc('black')
    )
    wc.generate_from_text(text, plot_now=False)
    # Show the image object wc_image
    st.image(wc.to_image())

    six_wc = swordcloud.SemanticWordCloud(language=lang,
        width = 1600,
        height = 800,
        max_font_size = 150,
        prefer_horizontal = 1,
        color_func = SingleColorFunc('black')
    )
    colors = ['black', 'navy', 'darkgreen', 'maroon', 'purple', 'teal']
    six_wc.generate_from_text(text, plot_now=False, kmeans=6)
    clouds = []
    for cloud, color in zip(six_wc.sub_clouds, colors):
        cloud.recolor(FrequencyColorFunc(color), plot_now=False)
        pil_img = cloud.to_image()
        clouds.append(pil_img)
    # Show images in clouds in 3x2 grid
    st.image(clouds, width=300)
    