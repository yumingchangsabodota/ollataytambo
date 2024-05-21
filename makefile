
remove:
	docker rmi ollataytambo:latest

build_local:
	docker build -f Dockerfile -t ollataytambo:latest .

run_api:
	docker run --env-file .env --rm --name ollataytambo_container \
	-v ./src:/app/src -v ./modules:/app/modules -v ./api:/app/api \
	-p 8086:8086 -it ollataytambo:latest uvicorn api.main:app --host 0.0.0.0 --port 8086 --reload