#!/bin/bash

echo "Iniciando despliegue del proyecto Virtualizacion de Redes..."
echo "Integracion: Docker + Flask + Asterisk"

echo "Construyendo contenedores..."
docker compose build

echo "Levantando contenedores..."
docker compose up -d

echo "Verificando contenedores en ejecucion..."
docker ps

echo "Proyecto desplegado exitosamente!"
echo "Flask disponible en: http://localhost:8000"
echo "Flask disponible en: http://localhost:8181"
echo "Flask disponible en: http://localhost:8888"
