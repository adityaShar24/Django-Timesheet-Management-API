FROM python:3.8.10-alpine
RUN apk add --no-cache gcc musl-dev

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV ENV=dev

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]