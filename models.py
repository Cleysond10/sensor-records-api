from sqlalchemy import DECIMAL, TIMESTAMP, Column, Integer, String
from database import Base


class Record(Base):
    __tablename__ = 'monitoring_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(String(50), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    value = Column(DECIMAL(10, 2), nullable=False)
