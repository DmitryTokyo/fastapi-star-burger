from pathlib import Path
import aiofiles
from fastapi import UploadFile

from backend.config.settings import settings


async def save_image_to_server(file: UploadFile) -> None:
    file_dir = Path(settings.MEDIA_ROOT) / "img"
    file_dir.mkdir(parents=True, exist_ok=True)
    file_path = file_dir / file.filename
    
    async with aiofiles.open(file_path, 'wb') as buffer:
        image_content = await file.read()
        await buffer.write(image_content)

