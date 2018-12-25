FROM python:3.6-jessie

ENV noninteractive=true

RUN apt-get update && \
	apt-get install -y apt-utils \
	apt-transport-https \
	locales \
	python3-dev \
	supervisor \
	nginx

WORKDIR /autocomplete_restapi

COPY ./requirements.txt /autocomplete_restapi/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /autocomplete_restapi/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \
    cp -r /autocomplete_restapi/conf/nginx.conf /etc/nginx/sites-available/default && \
    cp -r /autocomplete_restapi/conf/supervisor.conf /etc/supervisor/conf.d/ && \
    cp -r /autocomplete_restapi/conf/uwsgi.ini /autocomplete_restapi/

EXPOSE 6606
CMD ["supervisord"]