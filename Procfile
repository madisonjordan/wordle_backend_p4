traefik: ./proxy/traefik --configFile=./proxy/traefik.toml
checkings: uvicorn --port $CHECKING_PORT --app-dir="./api" checking_service:app --reload --root-path /api/checkings
validations: uvicorn --port $VALIDATION_PORT --app-dir="./api" validation_service:app --reload --root-path /api/validations
tracking: uvicorn --port $TRACKING_PORT --app-dir="./api" tracking_service:app
stats: uvicorn --port $PORT --app-dir="./api" statistics_service:app --reload --root-path /api/statistics
redis: redis-server
