# Базовый образ
FROM python:3.9-slim

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем приложение
COPY app.py .
COPY model.pkl .

# Указываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
