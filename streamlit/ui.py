import io

import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder

import streamlit as st


backend = "http://fastapi:8000/estimation"


# 传递图片至指定url
def process(image, server_url: str):
    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})  # 上传文件

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )  # 传递image至后端 返回r为处理后的图片

    return r


# construct UI layout
st.title("Human-estimation based on OpenPose")

st.write(
    """Obtain human—estimation maps of the image in input via OpenPose implemented in tensorflow.
         This streamlit example uses a FastAPI service as backend.
         Visit this URL at `:8000/docs` for FastAPI documentation."""
)  # description and instructions

input_image = st.file_uploader("insert image")  # image upload widget

if st.button("Get estimation map"):

    col1, col2 = st.columns(2)

    if input_image:
        estimate = process(input_image, backend)
        original_image = Image.open(input_image).convert("RGB")  # 原图片
        estimated_image = Image.open(io.BytesIO(estimate.content)).convert("RGB")
        col1.header("Original")  # 标题
        col1.image(original_image, use_column_width=True)

        col2.header("Estimated")  # 标题
        col2.image(estimated_image, use_column_width=True)

    else:
        # handle case with no image
        st.write("Insert an image!")
