from sqlalchemy import Column, Integer, String
from core.database import Base

class HallData(Base):
    __tablename__ = 'T001_MaschinenKanalBelegung'
    __table_args__ = {'schema': 'dbo'}

    id = Column(Integer, primary_key=True, nullable=False, name='ID')
    terminal_name = Column(String, nullable=False, name='TerminalName')
    terminal_name_2 = Column(String, nullable=True, name='Terminal2')
    hall = Column(String, nullable=False, name='Halle')
    pp_map_ip = Column(String, nullable=False, name='PPMapIP')
    
    def __repr__(self):
        return f"Terminal: {self.terminal_name}, Hall: {self.hall}, PP_Map_ID: {self.pp_map_id}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'terminal_name': self.terminal_name,
            'terminal_name_2': self.terminal_name_2,
            'hall': self.hall,
            'pp_map_ip': self.pp_map_ip
        }