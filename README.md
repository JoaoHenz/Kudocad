# Kudocad
<span style="font-size: larger;">KU</span>bernetes<br>
<span style="font-size: larger;">DO</span>cker <br>
<span style="font-size: larger;">C</span>osmos db<br>
<span style="font-size: larger;">A</span>zure<br>
<span style="font-size: larger;">D</span>jango<br>

# Dataset
Using this [free movies dataset](https://data.world/jamesgaskin/movies)

# Running with Docker
`docker compose up -d`<br>
Build and run the app in the background.

`docker compose down`<br>
Delete everything.

Access localhost:7010

# Running with Kubernetes

`docker-compose up --no-start`<br>
`kubectl apply -f k8s/deployment.yaml`<br>
`kubectl apply -f k8s/service.yaml`

Access localhost:30080
