from typing import Generic, List, TypeVar, final

from fastapi import Query
from pydantic import BaseModel

CollectionT = TypeVar('CollectionT')


class Pagination:
    def __init__(
        self,
        offset: int = Query(default=0, alias='page[offset]', ge=0),
        limit: int = Query(default=20, alias='page[limit]', ge=0, le=1000),
    ):
        self.offset = offset
        self.limit = limit


class Collection(BaseModel, Generic[CollectionT]):
    data: List[CollectionT]
    total: int


@final
class EmptyModel(BaseModel):
    pass
