from sqlalchemy import Column, Integer, String
from core.database import Base

class ProgramData(Base):
    __tablename__ = 'T001_Autostart'
    __table_args__ = {'schema': 'BB'}

    id = Column(Integer, primary_key=True, nullable=False, name='ID')
    client_name = Column(String, nullable=False, name='ClientName')
    active = Column(String, nullable=False, name='Active')
    program_name = Column(String, nullable=False, name='AppName')
    program_path = Column(String, nullable=False, name='AppPath')
    wait_until_restart_time = Column(Integer, nullable=False, name='WaitUntilRestartTime')
    status = Column(String, nullable=False, name='Status')
    in_menu = Column(String, nullable=False, name='InMenu')
    menu_name = Column(String, nullable=False, name='MenuName')
    program_image = Column(String, nullable=False, name='AppImage')
    last_check_time = Column(String, nullable=False, name='LastCheckTime')
    start_instruction = Column(String, nullable=False, name='StartInstruction')
    
    def __repr__(self):
        return f"Client: {self.client_name}, App: {self.program_name}, Status: {self.status}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'active': self.active,
            'program_name': self.program_name,
            'program_path': self.program_path,
            'wait_until_restart_time': self.wait_until_restart_time,
            'status': self.status,
            'in_menu': self.in_menu,
            'menu_name': self.menu_name,
            'program_image': self.program_image,
            'last_check_time': self.last_check_time,
            'start_instruction': self.start_instruction
        }