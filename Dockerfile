FROM python:3
ARG server_name=registration-server
WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

COPY ${server_name}/app.py .

EXPOSE 8080
CMD ["python3", "app.py"]
