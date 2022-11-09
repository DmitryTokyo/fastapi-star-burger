from fastapi.encoders import jsonable_encoder
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.foodcart.models.banners import Banner
from backend.foodcart.schemas.banners import BannerIn


async def get_banners(db: AsyncSession) -> list[Banner]:
    stmt = select(Banner)
    db_execute = await db.execute(stmt)
    return db_execute.scalars().all()


async def create_banner(db: AsyncSession, banner_in: BannerIn, picture_filename: str) -> Banner:
    banner_in_data = jsonable_encoder(banner_in)
    banner_in_data |= {'image_file': picture_filename}
    banner_obj = Banner(**banner_in_data)
    db.add(banner_obj)
    await db.commit()
    await db.refresh(banner_obj)
    return banner_obj


async def delete_banner(db: AsyncSession, banner_id: int) -> None:
    stmt = delete(Banner).where(Banner.id == banner_id)
    await db.execute(stmt)
    await db.commit()
