from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from starlette.status import HTTP_404_NOT_FOUND

from backend.config.settings import settings

router = APIRouter()


@router.get('/{filename}', responses={200: {'content': {'image/png': {}}}})
async def get_image(filename: str) -> FileResponse | None:
    file_path = f'{settings.MEDIA_ROOT}img/{filename}'
    image_file = Path(file_path)
    if not image_file.is_file():
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='File not found')
    return FileResponse(file_path)
