#!/bin/bash

# 定义一些变量
IMAGE_NAME="dify-app:v1"
CONTAINER_NAME="dify-app"
HOST_PORT=8553
CONTAINER_PORT=8553
# ENV_VAR="MY_ENV_VAR=production"

# 检查是否有同名的容器正在运行，如果有则停止并删除
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing the existing container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

if [ "$(docker ps -a -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing the existing container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# 运行新的容器
echo "Running a new container from the image $IMAGE_NAME"
docker run -d \
    -v ./:/app \
    --name $CONTAINER_NAME \
    -p $HOST_PORT:$CONTAINER_PORT \
    $IMAGE_NAME\
    python /app/main.py

# 检查容器状态
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Container $CONTAINER_NAME is running on port $HOST_PORT"
else
    echo "Failed to start the container $CONTAINER_NAME"
fi