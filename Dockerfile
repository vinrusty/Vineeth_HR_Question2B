FROM python:latest
WORKDIR /app
COPY . /app/
RUN pip install flask
CMD ["python","app.py"]