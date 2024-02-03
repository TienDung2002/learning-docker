FROM node:12.18-alpine

WORKDIR /app

RUN npm install -g pm2

COPY . .

RUN npm install

CMD ["pm2-runtime", "ecosystem.config.js"]
