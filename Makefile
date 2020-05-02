build:
	docker build -t contact-api:latest .

install:
	kubectl apply -f kubedeploy/secret.yml 
	kubectl apply -f kubedeploy/postgres-service.yml 
	kubectl apply -f kubedeploy/redis-service.yml 
	kubectl apply -f kubedeploy/webapp-service.yml 
	kubectl apply -f kubedeploy/postgres-deployment.yml 
	kubectl apply -f kubedeploy/redis-deployment.yml 
	kubectl apply -f kubedeploy/webapp-deployment.yml
	kubectl apply -f kubedeploy/celery-worker.yml

uninstall:
	kubectl delete secrets contact-api-secret
	kubectl delete services postgres-service 
	kubectl delete services redis-service 
	kubectl delete services webapp-service 
	kubectl delete deployment postgres-deployment 
	kubectl delete deployment redis-deployment 
	kubectl delete deployment webapp-deployment 
	kubectl delete deployment celery-worker