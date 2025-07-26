# Используем официальный Python образ
FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Указываем переменную среды для запуска FastAPI
ENV OPENAI_API_KEY=your_dummy_key  # на Render заменится переменной окружения

# Запускаем Streamlit
CMD ["streamlit", "run", "frontend/app.py", "--server.port=10000", "--server.enableCORS=false"]
