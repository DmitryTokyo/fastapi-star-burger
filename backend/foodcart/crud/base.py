from typing import TypeVar, Generic, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.db_init import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_single(self, db: AsyncSession, obj_id: int) -> ModelType:
        stmt = select(self.model).where(self.model.id == obj_id)
        db_execution = await db.execute(stmt)
        return db_execution.scalar_one()

    async def get_multi(self, db: AsyncSession) -> list[ModelType]:
        stmt = select(self.model)
        db_execution = await db.execute(stmt)
        return db_execution.scalars().all()

    async def create(self, db: AsyncSession, schema_in: CreateSchemaType, **kwargs) -> ModelType:
        obj_in_data = jsonable_encoder(schema_in)
        obj_in_data |= kwargs
        stmt = insert(self.model).values(**obj_in_data)
        db_execution = await db.execute(stmt)
        await db.commit()
        stmt = select(self.model).where(self.model.id == db_execution.inserted_primary_key[0])
        db_execution = await db.execute(stmt)
        return db_execution.scalar_one()

    async def update(self, db: AsyncSession, schema_update: UpdateSchemaType, obj_id: int) -> ModelType:
        obj_update_data = schema_update.dict(exclude_unset=True)
        stmt = update(self.model).where(self.model.id == obj_id).values(obj_update_data)
        await db.execute(stmt)
        await db.commit()

    async def delete(self, db: AsyncSession, obj_id: int) -> int:
        stmt = delete(self.model).where(self.model.id == obj_id)
        await db.execute(stmt)
        await db.commit()
        return obj_id
