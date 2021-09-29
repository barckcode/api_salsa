from fastapi import FastAPI

# Internal Modules
from routes.singers import singers_routes
from routes.songs import songs_routes

# Init FastAPI
app = FastAPI(
    title = "Salsa API",
    description = "Enpoints para descubrir cantantes y sus canciones más reconocidas",
    version = "0.1",
    contact = {
        "name": "Helmcode",
        "url": "https://helmcode.com/contact",
    },
    openapi_tags = [
        {
            "name": "Cantantes",
            "description": "Enpoint de Cantantes"
        },
        {
            "name": "Canciones",
            "description": "Enpoint de Canciones"
        }
    ]
)


# Include Routes to FastAPI
app.include_router(singers_routes)
app.include_router(songs_routes)
