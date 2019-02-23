docker-compose --file docker-compose.yml down -v --remove-orphans
docker-compose --file docker-compose.yml up -d --timeout=180 --build --force-recreate