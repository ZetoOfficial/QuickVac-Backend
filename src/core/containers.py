from dependency_injector import containers, providers

from quick_vac.repositories.skill_repository import SkillRepository
from quick_vac.repositories.vacancy_repository import VacancyRepository
from quick_vac.repositories.vacancy_skill_repository import VacancySkillRepository

from .database import Database, Transaction
from .settings import Settings, settings


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(Database, dsn=settings.DATABASE_DSN)

    transaction_provider = providers.Factory(
        Transaction,
        transaction_session=db.provided.transaction,
    )

    vacancy_repository = providers.Factory(VacancyRepository, session_factory=db.provided.session)
    skill_repository = providers.Factory(SkillRepository, session_factory=db.provided.session)
    vacancy_skill_repository = providers.Factory(VacancySkillRepository, session_factory=db.provided.session)


def configure(app_settings: Settings) -> Container:
    container = Container()
    return container
