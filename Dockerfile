FROM python:3.9

# 设置工作目录
WORKDIR /app

# 安装依赖
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyinstaller

# 将代码复制到容器中
COPY pythonTest.py .

# 构建可执行文件
RUN pyinstaller --onefile pythonTest.py

RUN useradd -ms /bin/bash myuser
# 设置容器用户的UID和GID
RUN usermod -u 1000 myuser && groupmod -g 1000 myuser
USER myuser

# 运行可执行文件
CMD ["./dist/pythonTest","--name","Matt"]