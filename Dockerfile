FROM python:3.12.4-slim

WORKDIR /app

COPY main.py ./
COPY fun_module.py ./
COPY config ./config
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
