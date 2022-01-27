FROM python:latest
        
COPY . WebApp-Core

WORKDIR /WebApp-Core/

RUN pip install -r requirements.txt
RUN flask db migrate -d database
RUN flask db upgrade -d database

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=localhost
ENV FLASK_RUN_PORT=5000

ENTRYPOINT ["flask", "run"]
