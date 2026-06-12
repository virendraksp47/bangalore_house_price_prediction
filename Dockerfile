FROM python:3.13
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5001", "main:app"]