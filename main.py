import streamlit as st
import pandas as pd
import torch
import torch.nn as nn
import torchvision

st.write('BrainScan')
uploaded_file = st.file_uploader("Choose an image")

genre = st.radio(
    "Choose a model",
    ["Xception", "Custom CNN"],
    captions=[
        "Powerful predictions",
        "Less memory & faster predictions",
    ],
)
