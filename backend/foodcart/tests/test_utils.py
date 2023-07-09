from pathlib import Path

import pytest
from backend.star_burger.utils.images import save_image_to_server
from backend.config.settings import settings


@pytest.mark.asyncio
async def test_save_image_to_server(mock_upload_file):
    await save_image_to_server(mock_upload_file)

    expected_path = Path(settings.MEDIA_ROOT) / 'img' / mock_upload_file.filename
    assert expected_path.exists()
    assert expected_path.read_text() == 'test_content'


    