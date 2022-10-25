from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.db_deps import get_db
from backend.foodcart.crud.crud_products import get_products, create_product, get_product_categories, \
    create_product_category
from backend.foodcart.schemas.products import ProductOut, ProductIn, ProductCategoryOut, ProductCategoryIn
from backend.foodcart.services.images import save_image

router = APIRouter()


@router.get('/', response_model=list[ProductOut])
async def read_products(db: AsyncSession = Depends(get_db)) -> list[ProductOut]:
    return await get_products(db)


@router.post('/', status_code=201)
async def create_new_banner(
    product_picture: UploadFile,
    product_in: ProductIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, ProductOut | str]:
    await save_image(product_picture)
    product = await create_product(db, product_in, product_picture.filename)
    return {'filename': product_picture.filename, 'banner': product}


@router.get('/categories/', response_model=list[ProductOut])
async def read_product_categories(db: AsyncSession = Depends(get_db)) -> list[ProductCategoryOut]:
    return await get_product_categories(db)


@router.post('/categories/', response_model=ProductCategoryIn, status_code=201)
async def create_new_restaurant(
        restaurant_in: ProductCategoryIn,
        db: AsyncSession = Depends(get_db),
) -> ProductCategoryOut:
    return await create_product_category(db, restaurant_in)
