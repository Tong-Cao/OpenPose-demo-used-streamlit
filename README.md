# OpenPose-demo-used-streamlit
使用**streamlit**以及**fastapi**来搭建前后端用来展示**OpenPose**处理结果的简单例程  

直接下载压缩文件，在创建镜像过程中可能会报错，建议采用本地仓库拉取方式  

运行前先安装好**docker**以及**compose**

运行终端打开文件位置输入`docker compose build`在本地创建镜像  

镜像创建完成后输入`docker compose up`创建容器并运行  
***
若不使用**docker**，可根据`安装过程.txt`中步骤手动进行环境配置  
在**fastapi**文件夹中的**openpose.py**中可以更换模型，其中**cmu**模型识别效果最好  
如需使用**cmu**模型请在`./fastapi/models/graph/cmu`中运行`.sh`文件进行模型下载，并在**openpose.py**中完成模型选择
