from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .util import lifetime, cors_config, CookieInitializationMiddleware
from .features.root.view import root
from fastapi import FastAPI

app = FastAPI(lifespan=lifetime)

app.mount("/img", StaticFiles(directory="./static/img"), name="img")
app.mount("/js", StaticFiles(directory="./static/js"), name="js")
app.add_middleware(CORSMiddleware, **cors_config)
app.add_middleware(CookieInitializationMiddleware)


app.include_router(root)
