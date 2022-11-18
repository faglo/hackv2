from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.app import holder_router


app = FastAPI()
app.include_router(holder_router, prefix="/electro_cars/api/v1", tags=["electro_cars"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.middleware("http")
# async def check_token(r: Request, call_next):
#     resp: Response = await call_next(r)
#     unauth_resp = JSONResponse({
#         "error": True,
#         "status": "Unauthorized",
#     },
#         headers={
#         "Access-Control-Allow-Origin": "*",
#         "Access-Control-Allow-Methods": "*",
#         "Access-Control-Allow-Headers": "authentication",
#     })

#     if "authentication" not in r.headers.keys() or not JWTService().verify_jwt(r.headers['authentication']):
#         return unauth_resp
#     return resp


@app.on_event("startup")
async def startup():
    print("API startup")


@app.on_event("shutdown")
async def shutdown():
    print("API shutdown")
