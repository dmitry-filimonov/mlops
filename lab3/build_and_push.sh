#!/bin/bash
# Автоматизация сборки образа и загрузки в DockerHub

# Получение текущего SHA коммита
GIT_SHA=$(git rev-parse --short HEAD)

# Построение Docker образа с тегом, включающим SHA коммита
docker build -t dmitryfilimonov/my_ml_model:$GIT_SHA -t dmitryfilimonov/my_ml_model:latest .

# Авторизация в DockerHub
echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin

# Публикация образа в DockerHub
docker push dmitryfilimonov/my_ml_model:$GIT_SHA
docker push dmitryfilimonov/my_ml_model:latest
