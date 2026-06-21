FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

WORKDIR /app/app

CMD ["python", "-m", "telegram_bot.bot"]