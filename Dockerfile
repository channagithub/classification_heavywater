FROM python:3.5.3

WORKDIR /app/

RUN apt update
RUN apt install -y supervisor
RUN pip install gunicorn setuptools

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

RUN mkdir -p /usr/intermediate

COPY unzip_data_file.py /app/
COPY data/shuffled-full-set-hashed.csv.zip /app/data/
RUN python unzip_data_file.py

COPY build_tokenizer.py /app/
RUN python build_tokenizer.py

# Setup supervisord
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /var/log/heavywater
COPY heavywater_configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY heavywater_configs/heavywater.conf /etc/supervisor/conf.d/

COPY . /app/