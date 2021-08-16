start:
	# start frontend
	cd ./frontend && yarn && yarn start

build: 
	# start backend
	docker compose up --build