build:
	docker build -t contact-api:latest .

install:
	kubectl apply -f kubedeploy/secret.yml --namespace=rqmp
	kubectl apply -f kubedeploy/postgres-service.yml --namespace=rqmp
	kubectl apply -f kubedeploy/redis-service.yml --namespace=rqmp
	kubectl apply -f kubedeploy/webapp-service.yml --namespace=rqmp
	kubectl apply -f kubedeploy/postgres-deployment.yml --namespace=rqmp
	kubectl apply -f kubedeploy/redis-deployment.yml --namespace=rqmp
	kubectl apply -f kubedeploy/webapp-deployment.yml --namespace=rqmp

uninstall:
	kubectl delete secrets contact-api-secret --namespace=rqmp
	kubectl delete services postgres-service --namespace=rqmp
	kubectl delete services redis-service --namespace=rqmp
	kubectl delete services webapp-service --namespace=rqmp
	kubectl delete deployment postgres-deployment --namespace=rqmp
	kubectl delete deployment redis-deployment --namespace=rqmp
	kubectl delete deployment webapp-deployment --namespace=rqmp
