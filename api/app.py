from fastapi import FastAPI
from routes.singers import singers

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
        }
    ]
)


# Include Routes to FastAPI
app.include_router(singers)
