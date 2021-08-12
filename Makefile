start:
	# start frontend
	cd ./frontend && yarn && yarn start
	# start the backend
	docker compose up

build: 
	docker compose up --build