from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.admin.admin import BannerAdmin
from backend.config.settings import settings
from backend.db.db_init import engine
from backend.exceptions import validation_schema_exception_handler
from backend.foodcart.api.routers import api_router
from backend.star_burger.routers import router

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount('/static', StaticFiles(directory='frontend/bundles'), name='static')
templates = Jinja2Templates(directory='frontend/public')

app.add_exception_handler(RequestValidationError, validation_schema_exception_handler)


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
async def init_template(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(router)

admin = Admin(app, engine)
admin.add_view(BannerAdmin)
