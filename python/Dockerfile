# 使用 python:3.8 作为基础镜像
FROM python:3.8-slim

# 手动创建 /etc/apt/sources.list 文件，并更换为阿里云源
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free" > /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-f" >> /etc/apt/sources.list
RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y build-essential libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app
# 复制当前文件夹所有内容到工作目录
# COPY . /app

# 使用豆瓣镜像源并安装依赖
# RUN pip install --no-cache-dir -i http://pypi.douban.com/simple --trusted-host pypi.douban.com fastapi uvicorn pydantic dify
RUN pip install  fastapi uvicorn dify_client -i https://pypi.tuna.tsinghua.edu.cn/simple
# 暴露应用的端口
EXPOSE 8553
EXPOSE 8000
# 运行 FastAPI 应用
# CMD ["python main.py"]