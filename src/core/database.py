from contextlib import AbstractContextManager, contextmanager
from typing import Callable, Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class _Base(object):
    def as_dict(self, excluded_cols: list[str] = []) -> dict:
        cols = dict(self.__dict__)
        cols.pop('_sa_instance_state', None)
        for col in excluded_cols:
            cols.pop(col, None)
        return cols

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


Base = declarative_base(cls=_Base)


class Database:
    def __init__(self, dsn: str) -> None:
        self._engine = create_engine(dsn)
        self._session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                expire_on_commit=False,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def transaction(self) -> Generator[Session, None, None]:
        session: Session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
            self._session_factory.remove()


class Transaction:
    def __init__(self, transaction_session: Callable[[], AbstractContextManager[Session]]):
        self.transaction = transaction_session
