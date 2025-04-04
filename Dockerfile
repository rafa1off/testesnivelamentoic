FROM python:3.13

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

EXPOSE 8000

ENTRYPOINT [ "fastapi", "run", "main.py", "--port", "8000" ]
