docker compose up --build --watch


docker compose down -v

docker compose up

///Probar post desde cmd
curl.exe -X POST "http://localhost:8080/api/chat/" -H "Content-Type: application/json" -d "{\"message\": \"Give me a summary of why it is good to go outside\"}"

//Instalar curl en container
apt-get -y update; apt-get -y install curl

//Ejecutar desde container modelo
curl http://model-runner.docker.internal/engines/v1/chat/completions -H "Content-Type: application/json" -d "{\"model\": \"ai/gemma3\", \"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"Please write 500 words about the fall of Rome.\"}]}"


//Ejecutar desde cmd modelo
curl http://localhost:12434/engines/v1/chat/completions -H "Content-Type: application/json" -d "{\"model\": \"ai/gemma3\", \"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"Please write 500 words about the fall of Rome.\"}]}"



//Correr contenedor
docker compose run backend /bin/bash  