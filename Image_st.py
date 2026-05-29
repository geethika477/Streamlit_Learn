import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

img = Image.open("calc.webp")

st.title("Image Operations on calc.webp")

st.subheader("Original Image")
st.image(img)

resize_img = img.resize((300,300))
st.subheader("Resized Image")
st.image(resize_img)

crop_img = img.crop((50,50,300,300))
st.subheader("Cropped Image")
st.image(crop_img)

rotate_img = img.rotate(90)
st.subheader("Rotated Image")
st.image(rotate_img)

flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
st.subheader("Flipped Image")
st.image(flip_img)

blur_img = img.filter(ImageFilter.BLUR)
st.subheader("Blur Effect")
st.image(blur_img)

sharp_img = img.filter(ImageFilter.SHARPEN)
st.subheader("Sharpen Effect")
st.image(sharp_img)

edge_img = img.filter(ImageFilter.FIND_EDGES)
st.subheader("Edge Detection")
st.image(edge_img)

gray_img = img.convert("L")
st.subheader("Black & White")
st.image(gray_img)

brightness = st.slider("Brightness",0.5,3.0,1.0)

enhancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(brightness)

st.subheader("Brightness Changed")
st.image(bright_img)

contrast = st.slider("Contrast",0.5,3.0,1.0)

contrast_enhancer = ImageEnhance.Contrast(img)
contrast_img = contrast_enhancer.enhance(contrast)

st.subheader("Contrast Changed")
st.image(contrast_img)

draw_img = img.copy()

draw = ImageDraw.Draw(draw_img)

draw.rectangle((50,50,250,250),outline="red",width=5)

st.subheader("Rectangle Drawn")
st.image(draw_img)

text_img = img.copy()

draw_text = ImageDraw.Draw(text_img)

draw_text.text((50,50),"Hello Streamlit",fill="white")
