FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN groupadd -r moda \
    && useradd -r -g moda moda

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements




COPY ./compose/production/trt/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh
RUN chown moda /gunicorn.sh

COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown moda /entrypoint.sh

COPY . /app
#RUN mkdir /logs /static

RUN chown -R moda /app

USER moda

WORKDIR /app


ENTRYPOINT ["/entrypoint.sh"]