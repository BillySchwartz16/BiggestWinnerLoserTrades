#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get update && apt-get install -y cron




#
COPY ./src /code/src


WORKDIR /code/src


#
CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "80"]