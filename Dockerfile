FROM python:3.11.4-slim-bullseye as prod

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copying requirements của project
COPY requirements.txt /app/src/
WORKDIR /app/src

# Cài đặt dependencies sử dụng pip
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

# Xoá gcc để giảm kích thước image
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copy mã nguồn của ứng dụng
COPY . /app/src/

CMD ["/usr/local/bin/python", "-m", "app"]

FROM prod as dev

# Nếu cần thêm các thư viện phục vụ phát triển (dev), có thể thêm file requirements-dev.txt
# RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements-dev.txt