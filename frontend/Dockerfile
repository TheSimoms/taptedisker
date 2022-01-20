FROM node:14-alpine AS base

WORKDIR /app

COPY rollup.config.js ./
COPY tsconfig.json ./
COPY package*.json ./

RUN npm install

COPY ./public ./public
COPY ./src ./src

ARG API_HOST
ENV API_HOST=$API_HOST

EXPOSE 5000
ENV HOST=0.0.0.0

ENTRYPOINT ["npm"]
CMD ["run", "dev"]

FROM base AS prod

RUN npm run build
