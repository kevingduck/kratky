from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Bin(db.Model):
    __tablename__ = 'bins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gallons = db.Column(db.Integer)
    plant_spaces = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    plants = db.relationship('Plant', backref='bin', lazy=True)

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    bin_id = db.Column(db.Integer, db.ForeignKey('bins.id'))
    name = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    expected_harvest_date = db.Column(db.Date)
    expected_harvest_amount = db.Column(db.Float)
    status = db.Column(db.String(20))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    bin_ids = db.Column(db.String(255), nullable=True)  # Store related bin IDs as a comma-separated string

    def get_bin_ids(self):
        """Returns a list of bin IDs as integers."""
        return [int(bin_id) for bin_id in self.bin_ids.split(',')] if self.bin_ids else []

    def get_bin_names(self):
        """Returns a list of bin names associated with this log."""
        bin_ids = self.get_bin_ids()
        bins = Bin.query.filter(Bin.id.in_(bin_ids)).all()
        return [bin.name for bin in bins]
