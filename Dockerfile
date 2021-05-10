FROM python:3

WORKDIR /urs/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/katorov/bjb-api
RUN pip install git+https://github.com/katorov/bjb-toolkit
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]