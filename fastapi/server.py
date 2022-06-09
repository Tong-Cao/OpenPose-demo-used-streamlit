import io


from starlette.responses import Response

from fastapi import FastAPI, File
from openpose import estimation_process


app = FastAPI(
    title="Human-estimation based on OpenPose",

    description="""Obtain human—estimation maps of the image in input via OpenPose implemented in tensorflow.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)


@app.post("/estimation")
def get_estimation_map(file: bytes = File(...)):
    """Get estimation maps from image file"""
    estimated_image = estimation_process(file)  # 输入openpose网络处理的到处理后的图片
    bytes_io = io.BytesIO()
    estimated_image.save(bytes_io, format="PNG")
    return Response(bytes_io.getvalue(), media_type="image/png")



