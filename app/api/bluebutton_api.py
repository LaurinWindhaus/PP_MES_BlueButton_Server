from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from crud.bluebutton_crud import get_program_data, get_hall_number, update_program_status, get_pp_map_ip
from schemas.bluebutton_schema import ProgramDataResponseSchema, HallNumberResponseSchema, PPMapIPResponseSchema, UpdateProgramStatusRequestSchema
from core.database import get_db

router = APIRouter()

@router.get("/programs/{client_name_to_retrieve}", response_model=List[ProgramDataResponseSchema])
def get_program_data_route(client_name_to_retrieve, db: Session = Depends(get_db)):
    program_data = get_program_data(client_name_to_retrieve, db)
    if program_data == None:
        raise HTTPException(status_code=404, detail="No Programs found for client")
    return program_data

@router.get("/hall_number/{client_name_to_retrieve}", response_model=HallNumberResponseSchema)
def get_hall_number_route(client_name_to_retrieve, db: Session = Depends(get_db)):
    hall_number = get_hall_number(client_name_to_retrieve, db)
    if hall_number == None:
        raise HTTPException(status_code=404, detail="Hall number not found")
    return hall_number

@router.get("/pp_map_ip/{client_name_to_retrieve}", response_model=PPMapIPResponseSchema)
def get_pp_map_ip_route(client_name_to_retrieve, db: Session = Depends(get_db)):
    pp_map_ip = get_pp_map_ip(client_name_to_retrieve, db)
    if pp_map_ip == None:
        raise HTTPException(status_code=404, detail="PP Map IP not found")
    return pp_map_ip

@router.post("/update_program_status", status_code=status.HTTP_200_OK)
def update_program_status_route(update_program_status_request: UpdateProgramStatusRequestSchema, db: Session = Depends(get_db)):
    updated_program_status = update_program_status(update_program_status_request.client_name, update_program_status_request.program_name, update_program_status_request.status, db)
    if updated_program_status == None:
        raise HTTPException(status_code=404, detail="Error updating program status")
    return updated_program_status