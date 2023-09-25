import sqlalchemy as sq
import sqlalchemy.orm as sqo
Class_base = sqo.declarative_base()
class score (Class_base):
    __tablename__ = 'Player'
    id = sq.Column(sq.Integer,primary_key=True)
    name = sq.Column(sq.String(255))
    size = sq.Column(sq.Integer)
base = sq.create_engine('sqlite:///base.db')
Class_base.metadata.create_all(base)