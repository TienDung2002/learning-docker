# build stage
FROM node:alpine3.19 as build-stage
WORKDIR /app
COPY . .
RUN npm install && npm run build

# production stage
FROM nginx:alpine3.18 as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

