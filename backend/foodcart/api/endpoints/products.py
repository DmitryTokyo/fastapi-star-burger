from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.db_deps import get_db
from backend.foodcart.crud.crud_products import get_products, create_product, get_product_categories, \
    create_product_category, delete_product_category
from backend.foodcart.schemas.products import ProductOut, ProductIn, ProductCategoryOut, ProductCategoryIn
from backend.star_burger.utils.images import save_image

router = APIRouter()


@router.get('/', response_model=list[ProductOut])
async def read_products(db: AsyncSession = Depends(get_db)):
    return await get_products(db)


@router.post('/', status_code=201)
async def create_new_product(
    product_picture: UploadFile,
    product_in: ProductIn = Depends(),
    db: AsyncSession = Depends(get_db),
) -> dict[str, ProductOut | str]:
    await save_image(product_picture)
    product = await create_product(db, product_in, product_picture.filename)
    return {'filename': product_picture.filename, 'banner': product}


@router.get('/categories/', response_model=list[ProductCategoryOut])
async def read_product_categories(db: AsyncSession = Depends(get_db)):
    print(ProductCategoryOut.schema())
    return await get_product_categories(db)


@router.post('/categories/', response_model=ProductCategoryOut, status_code=201)
async def create_new_product_category(
        category_in: ProductCategoryIn,
        db: AsyncSession = Depends(get_db),
):
    return await create_product_category(db, category_in)


@router.delete('/categories/', status_code=204)
async def delete_exist_product_category(category_id: int, db: AsyncSession = Depends(get_db)) -> None:
    return await delete_product_category(db, category_id)
