# Pulling ubuntu image with a specific tag from the docker hub.
FROM ubuntu:18.04

# Updating the packages and installing cron and vim editor if you later want to edit your script from inside your container.
RUN apt-get update \
&& apt-get install cron -y && apt-get install vim -y && apt-get install curl -y

# Crontab file copied to cron.d directory.
COPY cronjob /etc/cron.d/container_cronjob

# Script file copied into container.
COPY entrypoint.sh /entrypoint.sh

COPY insert_gainers.sh /insert_gainers.sh

# Giving executable permission to script file.
RUN chmod +x /entrypoint.sh
RUN chmod +x /insert_gainers.sh

# Running commands for the startup of a container.
CMD ["/bin/bash", "-c", "/entrypoint.sh && chmod 644 /etc/cron.d/container_cronjob && cron && tail -f /var/log/cron.log"]