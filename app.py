from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.app import holder_router
from services.logging import configure_logger, add_log_context, get_logger


app = FastAPI(title="AlfaBit.HolderAPI")
configure_logger()
app.include_router(holder_router, prefix="/holder/api/v1", tags=["holder"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(add_log_context)

logger = get_logger()

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
    logger.info("API startup")


@app.on_event("shutdown")
async def shutdown():
    logger.info("API shutdown")
