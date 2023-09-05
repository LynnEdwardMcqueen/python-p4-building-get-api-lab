from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_goods.bakeries',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.Integer, onupdate=db.func.now())
    baked_goods = db.relationship('BakedGood', backref='bakeries')
    def __repr__(self):
        return f'<Bakery {self.name} {self.id} {self.baked_goods}>'
    

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    serialize_rules = ('-bakeries.baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.Integer, onupdate=db.func.now())
    bakery_id = db.Column(db.Integer,db.ForeignKey('bakeries.id'))

    def __repr__(self):
        return f'<BakedGood {self.id} {self.name} price={self.price} bakery_id={self.bakery_id}>'
    
    