from contextlib import AbstractContextManager
from datetime import datetime
from typing import Callable

from sqlalchemy.orm import Session
from sqlalchemy.sql import func


class BaseRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    @staticmethod
    def delete_in_transaction(model, session: Session):
        session.delete(model)

    def delete(self, model):
        with self.session_factory() as session:
            session.delete(model)
            session.commit()

    def get_db_time(self) -> datetime:
        with self.session_factory() as session:
            return session.execute(func.now()).one()[0]

    @staticmethod
    def save_all_in_transaction(model, session: Session):
        session.add_all(model)
        session.flush()
        return model

    @staticmethod
    def save_in_transaction(model, session: Session):
        session.add(model)
        session.flush()
        return model

    @staticmethod
    def refresh(model, session: Session):
        session.refresh(model)
        return model

    def save(self, model):
        with self.session_factory() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model
