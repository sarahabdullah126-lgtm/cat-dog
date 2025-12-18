FROM python:3.11-slim
WORKDIR /app

# تثبيت تبعيات النظام الضرورية
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# تثبيت PyTorch وTorchVision باستخدام نسخة CPU (تسريع التحميل والحجم)
RUN pip install --no-cache-dir -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
