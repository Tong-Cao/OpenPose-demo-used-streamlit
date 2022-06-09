import sys
import time
from tf_pose import common
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
import io
from PIL import Image
import os


def estimation_process(binary_image):
    """
    post请求从streamlit拉取下来的图片为二进制，首先用io.BytesIO(binary_image)转为PIL处理格式
    openpose处理的图片格式为numpy.ndarray  所以这里先将PIL转numpy输入openpose网络，再将输出转PIL进行下一步处理
    """
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")  # io.BytesIO 为 bytes 转 PIL.Image.Image
    image = np.asarray(input_image)  # PIL.Image.Image转numpy.ndarray

    # 选择模型 help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small'
    e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(432, 368))  # 选择模型

    # estimate human poses from a single image !
    humans = e.inference(image, resize_to_default=0, upsample_size=4.0)
    # 输出人体关键点图片
    estimat_image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

    estimat_image = Image.fromarray(np.uint8(estimat_image))  # numpy.ndarray 转 PIL.Image.Image

    return estimat_image


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 忽略警告
    # 选择模型 help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small'
    e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(432, 368))

    # estimate human poses from a single image !
    image = common.read_imgfile('/home/tong/桌面/openpose_test/test-images/p1.jpg', None, None)  # arg.image根据上面输入参数选择图片
    # type(image) = numpy.ndarray

    t = time.time()  # 时间戳
    humans = e.inference(image, resize_to_default=0, upsample_size=4.0)

    elapsed = time.time() - t

    # 输出人体关键点图片
    image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
    # 展示结果图
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # 转换RGB颜色
    plt.show()


