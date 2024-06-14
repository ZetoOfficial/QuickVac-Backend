from uuid import UUID

from app.repositories import CRUDCompany
from app.schemas import CompanyDTO, InputCompanyDTO


class CompanyService:
    @staticmethod
    async def create_company(dto: InputCompanyDTO) -> CompanyDTO:
        return await CRUDCompany.create_company(dto)

    @staticmethod
    async def get_all_companies(limit: int = None, offset: int = None) -> list[CompanyDTO]:
        return await CRUDCompany.get_all_companies(limit, offset)

    @staticmethod
    async def get_company_by_id(company_id: UUID) -> CompanyDTO:
        return await CRUDCompany.get_company_by_id(company_id)

    @staticmethod
    async def update_company(company_id: UUID, dto: InputCompanyDTO) -> CompanyDTO:
        return await CRUDCompany.update_company(company_id, dto)

    @staticmethod
    async def delete_company(company_id: UUID) -> None:
        return await CRUDCompany.delete_company(company_id)
