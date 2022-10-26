import aiofiles
from fastapi import UploadFile

from backend.config.settings import settings


async def save_image(file: UploadFile) -> None:
    file_path = f'{settings.MEDIA_ROOT}img/{file.filename}'
    async with aiofiles.open(file_path, 'wb') as buffer:
        image_content = await file.read()
        await buffer.write(image_content)
