from fastapi import FastAPI
from routers import atleta_router
from fastapi_pagination import add_pagination

app = FastAPI(
    title="Workout API",
    version="1.0.0"
)

# Rotas
app.include_router(atleta_router.router)

# Paginação
add_pagination(app)
