# 使用官方 Node.js 镜像作为基础镜像
FROM node:18-alpine

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json（如果有）
COPY package*.json ./
RUN  npm config set registry https://registry.npmmirror.com

# 安装项目依赖
RUN npm install 
RUN npm install vite
# 如果你有构建步骤（例如前端打包），可以在这里运行
# RUN npm run build

# 复制应用的源代码到容器
# COPY . .

# 暴露应用使用的端口（例如：3000）
EXPOSE 5173

# 启动应用
# CMD ["npm", "start"]