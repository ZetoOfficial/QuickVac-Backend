COMPOSE := docker-compose -f docker/docker-compose.dev.yml

.PHONY: up
up:
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down -v

ps:
	$(COMPOSE) ps

logs:
	$(COMPOSE) logs -f --tail 100 api

migrate:
	$(COMPOSE) exec api alembic upgrade head