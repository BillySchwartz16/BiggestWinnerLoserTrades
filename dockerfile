FROM nickgryg/alpine-pandas:latest

VOLUME /data
COPY crontab.txt /crontab.txt
COPY entry.sh /entry.sh
COPY requirements.txt /opt/app/requirements.txt
RUN pip3 install --upgrade pip
RUN apk add --no-cache --virtual build-deps \
        build-base \
        && \
    pip3 install --no-cache --no-cache-dir --user --requirement /opt/app/requirements.txt && \
    apk del --no-cache build-deps && \
    :

COPY losers.py /opt/app/losers.py

RUN chmod 755 /opt/app/losers.py /entry.sh
RUN /usr/bin/crontab /crontab.txt

CMD ["/entry.sh"]