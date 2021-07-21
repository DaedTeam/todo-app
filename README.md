# cube-engine

sudo docker build --tag cube-engine .
sudo docker run -d -e PORT=8080 --publish 8080:8080 --name cube-engine-app cube-engine
sudo docker exec -it cube-engine-app bash

pip install -r requirements.txt
uvicorn --env-file .env app.main:app --port {port} --reload
