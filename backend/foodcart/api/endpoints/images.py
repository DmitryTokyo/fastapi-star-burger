from fastapi import APIRouter

router = APIRouter()


@router.get('/image', responses={200: {'content': {'image/png': {}}}})
async def get_image(filename: str):
    pass
