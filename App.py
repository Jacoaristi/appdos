import streamlit as st
import os
import time
import glob
import os
from gtts import gTTs
from PIL import Image

st.title("Interfaces Multimodales.")
image = Image.open('INTELESTELAR.jpg')

 st.image(image, width=200)                 


try:
  os.mkdir("temp")
except:
  pass

st.subheader("Texto a audio.")
st.write ('Las interfaces de texto a audio son fundamentales en las interfaces multimediales ya que permiten'
         'una comunicacion mas accesible y natural,facilitando la inclusion de personas con discapacidades'
         )
