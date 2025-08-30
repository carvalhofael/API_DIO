from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db.database import get_db
from repositories import atleta_repository
from schemas.atleta_schema import AtletaCreate, AtletaResponse
from fastapi_pagination import Page, paginate

router = APIRouter(prefix="/atletas", tags=["Atletas"])


@router.get("/", response_model=Page[AtletaResponse])
def get_atletas(
    nome: str | None = Query(None, description="Filtrar por nome"),
    cpf: str | None = Query(None, description="Filtrar por CPF"),
    db: Session = Depends(get_db)
):
    atletas = atleta_repository.get_all(db, nome=nome, cpf=cpf)
    return paginate(atletas)


@router.post("/", response_model=AtletaResponse)
def create_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    return atleta_repository.create(db, atleta)
