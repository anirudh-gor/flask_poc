from db import db
from datetime import datetime

class SolutionModel(db.Model):
    __tablename__ = 'solutions'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    poc = db.Column(db.String(200))
    contact_number = db.Column(db.Integer, default=1234567899)
    email = db.Column(db.String(200), default='test@test.com')
    location = db.Column(db.String(200))
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    region = db.relationship('RegionModel')
    currency = db.Column(db.String(200), default='INR')
    units = db.Column(db.String(200), default='imperical')
    channel_partner = db.Column(db.String(200), default='gor')
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
            'name' : self.name,
            'poc' : self.poc,
            'email' : self.email,
            'contact_number' : self.contact_number,
            'location' : self.location,
            'region_id' : self.region_id,
            'currency' : self.currency,
            'units' : self.units,
            'channel_partner' : self.channel_partner
        }
