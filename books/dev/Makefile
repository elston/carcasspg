all:
	@echo "Hello $(LOGNAME), nothing to do by default"

# ========= pool ==============
pool:
	@echo "---> pool postgres:9.5"
	@docker pull postgres:9.5
	@echo "---> pool python:3.4-slim"
	@docker pull python:3.4-slim
	@echo "---> pool nginx:1.11.13-alpine"	
	@docker pull nginx:1.11.13-alpine

# =========== build ================
build_storage:
	@docker-compose \
		-p carcasspg \
		-f build.yml \
		build storage

build_mediatry:
	@docker-compose \
		-p carcasspg \
		-f build.yml \
		build mediatry

build:
	@docker-compose \
		-p carcasspg \
		-f build.yml \
		build

rebuild:
	@docker-compose \
		-p carcasspg \
		-f build.yml \
		build --force-rm mediatry

clear:
	@../../scripts/clear_untagged.sh

# ========= bootstrap ==============
bootstrap_storage:
	@docker-compose \
		-p carcasspg \
		-f bootstrap.yml \
		run --rm storage

bootstrap_mediatry:
	@docker-compose \
		-p carcasspg \
		-f bootstrap.yml \
		run --rm mediatry /usr/local/bin/bootstrap.sh

bootstrap:
	@echo "---> bootstrap storage"
	@make bootstrap_storage
	@echo "---> bootstrap mediatry"	
	@make bootstrap_mediatry

# ==========  migrate =================
migrate_mediatry:
	@docker-compose \
		-p carcasspg \
		-f migrate.yml \
		run --rm mediatry /usr/local/bin/migrate.sh
	@echo "---> end session mediatry"			
	@make down

# =====================================
db:
	@docker-compose \
		-p carcasspg \
		-f db.yml \
		up -d --no-build --no-recreate

shell_mediatry:
	@docker-compose \
		-p carcasspg \
		-f run.yml \
		run --rm mediatry /bin/bash
	@echo "---> end session mediatry"	
	@make down	

devserv:
	@docker-compose \
		-p carcasspg \
		-f run.yml \
		run --rm mediatry /usr/local/bin/runserv.sh

# =========== logs =====================
log_mediatry:
	@docker logs -f carcasspg_mediatry_1

log_storage:
	@docker logs -f carcasspg_storage_1	

# ======================================
up:
	@docker-compose \
		-p carcasspg \
		-f run.yml \
		up -d --no-build --no-recreate
down:
	@docker-compose \
		-p carcasspg \
		-f run.yml \
		down	

restart:
	@make down
	@make up


ps:
	@docker-compose \
		-p carcasspg \
		-f run.yml \
		ps



