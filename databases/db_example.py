from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime, Boolean, ForeignKey
from datetime import datetime

from sqlalchemy.sql.schema import ForeignKey

Base =  declarative_base()

class Student(Base):
    __tablename__  = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    section = Column(String(1))
    klass = Column(String(4))
    is_online = Column(Boolean, default=False)
    admit_date = Column(Datetime,default=datetime.now())
    
    def __str__(self):
        return f"{self.name}{self.klass}{self.section}"
class Grade(Base):
    __tablename__ = 'student grade'
    student = Column(ForeignKey('students.id'))
    hindi = Column(Integer)
    maths = Column(Integer)
    english = Column(Integer)
    total = Column(Integer)
    date = Column(datetime,default=datetime.now())

    def __str__(self):
        return f"{self.total}{Pass if self.total > 120 else 'Fail'}"



