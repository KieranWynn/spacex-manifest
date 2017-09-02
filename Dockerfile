FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install -e .
CMD ["python", "spacex_manifest/app.py"]
