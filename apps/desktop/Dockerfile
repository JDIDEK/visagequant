FROM node:24-alpine AS dependencies

WORKDIR /workspace

RUN corepack enable \
    && corepack prepare pnpm@12.4.1 --activate

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/desktop/package.json ./apps/desktop/package.json
RUN pnpm install --frozen-lockfile

FROM dependencies AS development

COPY apps/desktop ./apps/desktop
WORKDIR /workspace/apps/desktop
EXPOSE 1420
CMD ["pnpm", "dev", "--host", "0.0.0.0"]

FROM dependencies AS build

COPY apps/desktop ./apps/desktop
WORKDIR /workspace/apps/desktop
ARG VITE_API_URL=http://127.0.0.1:8765
ENV VITE_API_URL=${VITE_API_URL}
RUN pnpm build

FROM nginx:1.27-alpine AS production

COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
