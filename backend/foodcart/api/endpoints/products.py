from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from backend.db.db_deps import get_db
from backend.foodcart.crud.crud_products import (
    get_products, create_product, get_product_categories, create_product_category, delete_product_category,
    delete_product, update_product_category,
)
from backend.foodcart.schemas.products import (
    ProductOut, ProductIn, ProductCategoryOut, ProductCategoryIn, ProductCategoryUpdate,
)
from backend.star_burger.utils.images import save_image_to_server

router = APIRouter()


@router.get('/', response_model=list[ProductOut], status_code=HTTP_200_OK)
async def read_products(db: AsyncSession = Depends(get_db)):
    return await get_products(db)


@router.post('/', status_code=HTTP_201_CREATED)
async def create_new_product(
    product_picture: UploadFile,
    product_in: ProductIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, ProductOut | str]:
    await save_image_to_server(product_picture)
    product = await create_product(db, product_in, product_picture.filename)
    return {'filename': product_picture.filename, 'banner': product}


@router.delete('/', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_product(product_id: int, db: AsyncSession = Depends(get_db)) -> None:
    return await delete_product(db, product_id)


@router.get('/categories/', response_model=list[ProductCategoryOut], status_code=HTTP_200_OK)
async def read_product_categories(db: AsyncSession = Depends(get_db)):
    return await get_product_categories(db)


@router.post('/categories/', response_model=ProductCategoryOut, status_code=HTTP_201_CREATED)
async def create_new_product_category(
        category_in: ProductCategoryIn,
        db: AsyncSession = Depends(get_db),
):
    return await create_product_category(db, category_in)


@router.delete('/categories/', status_code=204)
async def delete_exist_product_category(category_id: int, db: AsyncSession = Depends(get_db)) -> None:
    return await delete_product_category(db, category_id)


@router.patch('/categories/{product_categories_id}', response_model=ProductCategoryOut, status_code=HTTP_200_OK)
async def update_exist_product_category(
    product_category_id: int,
    product_category_update: ProductCategoryUpdate,
    db: AsyncSession = Depends(get_db)
):
    product_category_obj = await update_product_category(db, product_category_id, product_category_update)
    return product_category_obj
