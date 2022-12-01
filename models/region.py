from db import db
from datetime import datetime

class RegionModel(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Solution %r>' % self.id
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def search_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def persist(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_json(self):
        return {
            'name' : self.name
        }
