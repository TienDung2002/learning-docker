# build stage
FROM node:alpine3.19 as build-stage
WORKDIR /app
COPY . .
RUN npm install 
RUN npm run build

# production stage
FROM nginx:alpine3.18 as production-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"] 

# https://viblo.asia/p/dockerize-ung-dung-vuejs-reactjs-ORNZqxwNK0n