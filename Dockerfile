# 1. 地基：找一个装好了 Python 3.9 的 Linux 极简版作为基础
FROM python:3.9-slim

# 2. 目录：在容器内部创建一个叫 /app 的工作目录
WORKDIR /app

RUN pip install redis -i https://pypi.tuna.tsinghua.edu.cn/simple

# 3. 搬运：把当前目录下的 server.py 复制到容器里的 /app 目录
COPY server.py .

# 4. 启动：容器启动时，执行什么命令
CMD ["python", "server.py"]

