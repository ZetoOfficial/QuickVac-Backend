from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import CompanyDTO, InputCompanyDTO
from app.services import CompanyService

company_router = APIRouter()


@company_router.post("/companies", response_model=CompanyDTO)
async def create_company(dto: InputCompanyDTO):
    """Create a new company in the database"""
    try:
        return await CompanyService.create_company(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@company_router.get("/companies", response_model=list[CompanyDTO])
async def get_all_companies(limit: int = 100, offset: int = 0):
    """Get all companies from the database"""
    try:
        return await CompanyService.get_all_companies(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@company_router.get("/companies/{company_id}", response_model=CompanyDTO)
async def get_company_by_id(company_id: UUID):
    """Get a specific company by its ID"""
    try:
        return await CompanyService.get_company_by_id(company_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@company_router.put("/companies/{company_id}", response_model=CompanyDTO)
async def update_company(company_id: UUID, dto: InputCompanyDTO):
    """Update a specific company"""
    try:
        return await CompanyService.update_company(company_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@company_router.delete("/companies/{company_id}", response_model=None)
async def delete_company(company_id: UUID):
    """Delete a specific company"""
    try:
        await CompanyService.delete_company(company_id)
        return {"message": "Company deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
