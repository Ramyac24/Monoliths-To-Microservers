# Follow Task-0 subtask-1

FROM python:3.8-alpine

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN apk add --update
RUN pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt
RUN rm -rf /var/cache/apk/*

COPY ./app /app

#RUN python app.py
#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050"]
CMD ["python3", "app.py"]
