from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.app import router


app = FastAPI()
app.include_router(router, prefix="/electro_cars/api/v1", tags=["electro_cars"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    print("API startup")


@app.on_event("shutdown")
async def shutdown():
    print("API shutdown")
