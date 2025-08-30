from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.atleta_model import Atleta
from schemas.atleta_schema import AtletaCreate


def get_all(db: Session, nome: str | None = None, cpf: str | None = None):
    query = db.query(Atleta)

    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)

    return query.all()


def create(db: Session, atleta: AtletaCreate):
    db_atleta = Atleta(**atleta.dict())
    db.add(db_atleta)
    try:
        db.commit()
        db.refresh(db_atleta)
        return db_atleta
    except IntegrityError as e:
        db.rollback()
        if "cpf" in str(e.orig).lower():
            raise HTTPException(
                status_code=303,
                detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
            )
        raise
