FROM node:14.15

RUN mkdir /app

WORKDIR /app

COPY src /app

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
