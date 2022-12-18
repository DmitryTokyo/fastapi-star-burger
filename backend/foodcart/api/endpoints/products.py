from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from backend.db.db_deps import get_db
from backend.foodcart.schemas.products import (
    ProductOut, ProductIn, ProductCategoryOut, ProductCategoryIn, ProductCategoryUpdate, ProductUpdate,
)
from backend.star_burger.utils.images import save_image_to_server
from backend.foodcart.crud.product import crud_product, crud_product_category


router = APIRouter()


@router.get('/', response_model=list[ProductOut], status_code=HTTP_200_OK)
async def read_products(db: AsyncSession = Depends(get_db)):
    return await crud_product.get_multi(db)


@router.post('/', status_code=HTTP_201_CREATED)
async def create_new_product(
    product_picture: UploadFile,
    product_in: ProductIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, ProductOut | str]:
    await save_image_to_server(product_picture)
    product = await crud_product.create(db, product_in, image_url=product_picture.filename)
    return {'filename': product_picture.filename, 'banner': product}


@router.delete('/', status_code=HTTP_204_NO_CONTENT)
async def delete_exist_product(product_id: int, db: AsyncSession = Depends(get_db)) -> None:
    try:
        await crud_product.get_single(db, product_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')
    return await crud_product.delete(db, product_id)


@router.patch('/{product_id}', response_model=ProductOut, status_code=HTTP_200_OK)
async def update_exist_product(product_id: int, product_update: ProductUpdate, db: AsyncSession = Depends(get_db)):
    try:
        await crud_product.get_single(db, product_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')
    await crud_product.update(db, product_update, product_id)
    return crud_product.get_single(db, product_id)


@router.patch('/{produsct_id}/image', response_model=ProductOut, status_code=HTTP_200_OK)
async def update_exist_product_image(product_id: int, product_image: UploadFile, db: AsyncSession = Depends(get_db)):
    try:
        await crud_product.get_single(db, product_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')

    await save_image_to_server(product_image)
    product_update = ProductUpdate(image_url=product_image.filename)
    await crud_product.update(db, product_update, product_id)
    return await crud_product.get_single(db, product_id)


@router.get('/categories/', response_model=list[ProductCategoryOut], status_code=HTTP_200_OK)
async def read_product_categories(db: AsyncSession = Depends(get_db)):
    return await crud_product_category.get_multi(db)


@router.post('/categories/', response_model=ProductCategoryOut, status_code=HTTP_201_CREATED)
async def create_new_product_category(
        category_in: ProductCategoryIn,
        db: AsyncSession = Depends(get_db),
):
    return await crud_product_category.create(db, category_in)


@router.delete('/categories/', status_code=204)
async def delete_exist_product_category(product_category_id: int, db: AsyncSession = Depends(get_db)) -> None:
    try:
        await crud_product_category.get_single(db, product_category_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')
    return await crud_product_category.delete(db, product_category_id)


@router.patch('/categories/{product_categories_id}', response_model=ProductCategoryOut, status_code=HTTP_200_OK)
async def update_exist_product_category(
    product_category_id: int,
    product_category_update: ProductCategoryUpdate,
    db: AsyncSession = Depends(get_db),
):
    try:
        await crud_product_category.get_single(db, product_category_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Object does not found')

    await crud_product_category.update(db, product_category_update, product_category_id)
    return await crud_product_category.get_single(db, product_category_id)
