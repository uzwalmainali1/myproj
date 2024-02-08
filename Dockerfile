FROM python:3.7-alpine

WORKDIR /

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "-u", "main.py"]
