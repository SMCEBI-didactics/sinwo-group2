FROM python:latest

COPY . statystyka

WORKDIR statystyka/

#RUN pip install -r requirements.txt
RUN pip install .

ENTRYPOINT ["statystyka"]
