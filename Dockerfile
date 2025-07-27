FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY shared ./shared

# не хардкодим ключи, они придут из Render’а
# ENV OPENAI_API_KEY=...

# Слушаем PORT, который выставляет Render
CMD uvicorn backend.main:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend/app.py \
      --server.port $PORT \
      --server.address=0.0.0.0
