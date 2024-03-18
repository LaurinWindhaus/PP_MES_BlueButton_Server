from sqlalchemy.orm import Session
from models.ProgramData import ProgramData
from models.HallData import HallData
from sqlalchemy.orm import aliased


def get_program_data(client_name_to_retrieve: str, db: Session):
    try:
        return db.query(ProgramData).filter(ProgramData.client_name == client_name_to_retrieve).filter(ProgramData.active != "n").all()
    except Exception as e:
        print(e)
        return None
    
def get_hall_number(client_name_to_retrieve: str, db: Session):
    try:
        # Creating an alias for the HallData table for the second join
        HallDataAlias = aliased(HallData)
        
        return db.query(HallData.hall)\
            .outerjoin(ProgramData, (ProgramData.client_name == HallData.terminal_name) & (ProgramData.active != 'n'))\
            .outerjoin(HallDataAlias, (ProgramData.client_name == HallDataAlias.terminal_name_2) & (ProgramData.active != 'n'))\
            .filter(ProgramData.client_name == client_name_to_retrieve).first()
    except Exception as e:
        print(e)
        return None
    
def update_program_status(client_name_to_retrieve: str, program_name: str, new_status: str, db: Session):
    try:
        program_to_update = db.query(ProgramData)\
            .filter(ProgramData.client_name == client_name_to_retrieve)\
            .filter(ProgramData.program_name == program_name)\
            .first()

        if program_to_update:
            program_to_update.status = new_status
            db.commit()
            return program_to_update.status  
        else:
            return None
    except Exception as e:
        print(e)
        return None

def get_pp_map_ip(client_name_to_retrieve: str, db: Session):
    try:
        return db.query(HallData.pp_map_ip).filter(HallData.terminal_name == client_name_to_retrieve).first()
    except Exception as e:
        print(e)
        return None