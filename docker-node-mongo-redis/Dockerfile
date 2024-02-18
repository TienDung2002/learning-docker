FROM node:alpine3.19
WORKDIR /app
COPY . .
RUN npm install

# môi trường Development
CMD ["npm", "run", "dev"]

# môi trường Production
# RUN npm install -g pm2
# CMD ["pm2-runtime", "ecosystem.config.js", "--env", "production"]

# https://viblo.asia/p/dockerize-project-nodejs-mongodb-redis-passport-4P856NXW5Y3 
