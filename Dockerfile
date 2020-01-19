FROM python:latest
RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt .
COPY ./run.py .
COPY ./app ./app/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["run.py"]
EXPOSE 80