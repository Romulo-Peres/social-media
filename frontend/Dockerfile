
FROM node:18-slim AS build

WORKDIR /build

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

FROM node:18-slim

WORKDIR /app

COPY server/package.json server/package-lock.json ./

RUN npm install --production

COPY --from=build ./build/dist ./dist

COPY server/. ./

CMD ["node", "main.js"]