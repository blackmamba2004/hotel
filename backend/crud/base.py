from typing import Any, cast, Generic, Sequence, TypeVar, Type

from sqlalchemy import select, inspect, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapper

from backend.models.base import BaseModel
from backend.schemas.base import BaseSchema

ModelType = TypeVar("ModelType", bound=BaseModel)
CreatingSchemaType = TypeVar("CreatingSchemaType", bound=BaseSchema)
UpdatingSchemaType = TypeVar("UpdatingSchemaType", bound=BaseSchema)


class CRUDBase(Generic[ModelType, CreatingSchemaType, UpdatingSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> ModelType | None:
        return await db.get(self.model, id)
    
    async def get_by(self, db: AsyncSession, **kwargs) -> ModelType | None:
        return (
            await db.execute(
                select(self.model.__table__.columns).filter_by(**kwargs)
            )
        ).mappings().first()

    async def get_many(self, db: AsyncSession) -> Sequence[ModelType] | None:
        return (
            await db.execute(select(self.model.__table__.columns))
        ).mappings().all()

    async def _get_db_obj_fields(
        self, obj_in: dict[str, Any] | BaseSchema, **kwargs
    ) -> dict[str, Any]:
        if isinstance(obj_in, dict):
            data = obj_in
        else:
            data = obj_in.model_dump(exclude_unset=True)
        data.update(**kwargs)
        return data
    
    async def _set_db_obj_fields(
        self, db_obj: ModelType, fields: dict[str, Any]
    ) -> ModelType:
        info = cast(Mapper, inspect(self.model))
        for field in info.columns.keys() + info.relationships.keys():
            if field in fields:
                setattr(db_obj, field, fields[field])
        return db_obj
    
    async def create(
        self, db: AsyncSession, obj_in: CreatingSchemaType | dict[str, Any], **kwargs
    ) -> ModelType:
        db_obj = self.model()
        fields = await self._get_db_obj_fields(obj_in, **kwargs)
        db_obj = await self._set_db_obj_fields(db_obj, fields)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(
        self, db: AsyncSession, db_obj: ModelType, obj_in: UpdatingSchemaType, **kwargs
    ) -> ModelType:
        fields = await self._get_db_obj_fields(obj_in, **kwargs)
        db_obj = await self._set_db_obj_fields(db_obj, fields)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def delete(
        self, db: AsyncSession, **filter_by
    ):
        query = delete(self.model).filter_by(**filter_by)
        await db.execute(query)
        await db.commit()
