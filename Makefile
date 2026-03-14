 # =========================
# Sea Marine Fuels – Dev Runner
# =========================
COMPOSE := docker compose
COMPOSE_FILE := -f docker-compose.yml

.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Sea Marine Fuels (Root) Commands"
	@echo ""
	@echo "Lifecycle:"
	@echo "  make up                  Start all services"
	@echo "  make up-build            Build images + start services"
	@echo "  make down                Stop everything"
	@echo "  make restart             Restart everything (rebuild)"
	@echo "  make ps                  Container status"
	@echo "  make logs                Tail logs for all services"
	@echo ""
	@echo "Target logs:"
	@echo "  make logs-web            Django web service"
	@echo "  make logs-caddy          Caddy reverse-proxy"
	@echo ""
	@echo "Shell access:"
	@echo "  make sh-web              Shell into Django container"
	@echo "  make sh-caddy            Shell into Caddy container"
	@echo ""
	@echo "Django:"
	@echo "  make manage cmd=<command>     Run ./manage.py <command>"
	@echo "  make makemigrations           Create migrations"
	@echo "  make migrate                  Apply migrations"
	@echo "  make collectstatic            Collect static files"
	@echo "  make createsuperuser          Create Django super-user"
	@echo "  make shell                    Django shell (+autoload)"
	@echo ""

# =========================
# Lifecycle
# =========================
up:
	$(COMPOSE) $(COMPOSE_FILE) up -d

up-build:
	$(COMPOSE) $(COMPOSE_FILE) up -d --build

down:
	$(COMPOSE) $(COMPOSE_FILE) down

restart:
	$(COMPOSE) $(COMPOSE_FILE) down
	$(COMPOSE) $(COMPOSE_FILE) up -d --build

ps:
	$(COMPOSE) $(COMPOSE_FILE) ps

logs:
	$(COMPOSE) $(COMPOSE_FILE) logs -f --tail=200

logs-web:
	$(COMPOSE) $(COMPOSE_FILE) logs -f --tail=200 web

logs-caddy:
	$(COMPOSE) $(COMPOSE_FILE) logs -f --tail=200 caddy

# =========================
# Shell access
# =========================
sh-web:
	$(COMPOSE) $(COMPOSE_FILE) exec web bash

sh-caddy:
	$(COMPOSE) $(COMPOSE_FILE) exec caddy sh

# =========================
# Django shortcuts
# =========================
manage:
	@$(COMPOSE) $(COMPOSE_FILE) exec web python manage.py $(cmd)

makemigrations:
	$(COMPOSE) $(COMPOSE_FILE) exec web python manage.py makemigrations

migrate:
	$(COMPOSE) $(COMPOSE_FILE) exec web python manage.py migrate

collectstatic:
	$(COMPOSE) $(COMPOSE_FILE) exec web python manage.py collectstatic --noinput

createsuperuser:
	$(COMPOSE) $(COMPOSE_FILE) exec web python manage.py createsuperuser

shell:
	$(COMPOSE) $(COMPOSE_FILE) exec web python manage.py shell -c "import django; django.setup()" -i python