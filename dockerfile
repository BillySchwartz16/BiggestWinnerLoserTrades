FROM nickgryg/alpine-pandas:latest

VOLUME /data
COPY crontab.txt /crontab.txt
COPY entry.sh /entry.sh
COPY ./app/* /opt/app/
RUN pip3 install --upgrade pip
RUN apk add --no-cache --virtual build-deps \
        build-base \
        && \
    pip3 install --no-cache --no-cache-dir --user --requirement /opt/app/requirements.txt && \
    apk del --no-cache build-deps && \
    :

RUN chmod 755 /opt/app/losers.py /opt/app/winners.py /opt/app/analyze.py /entry.sh
RUN /usr/bin/crontab /crontab.txt

CMD ["/entry.sh"]