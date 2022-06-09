# OpenPose-demo-used-streamlit
使用**streamlit**以及**fastapi**来搭建前后端用来展示**OpenPose**处理结果的简单例程

运行前先安装好**docker**以及**compose**

运行终端打开文件位置输入`docker compose build`在本地创建镜像  

镜像创建完成后输入`docker compose up`创建容器并运行  
***
在fastapi文件夹中的openpose.py中可以更换模型，其中cmu模型识别效果最好  
如需使用cmu模型请在./fastapi/models/graph/cmu中运行.sh文件进行模型下载，并在openpose.py中完成模型选择
