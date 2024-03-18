from pydantic import BaseModel


class ProgramDataResponseSchema(BaseModel):
    client_name: str
    active: str
    program_name: str
    program_path: str
    wait_until_restart_time: int
    status: str
    in_menu: str
    menu_name: str
    program_image: str
    last_check_time: str
    start_instruction: str

class HallNumberResponseSchema(BaseModel):
    hall: int

class PPMapIPResponseSchema(BaseModel):
    pp_map_ip: str

class UpdateProgramStatusRequestSchema(BaseModel):
    client_name: str
    program_name: str
    status: str