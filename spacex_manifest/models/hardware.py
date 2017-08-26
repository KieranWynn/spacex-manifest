import sqlalchemy as sa
from sqlalchemy import orm

from .base import ModelBase
from .model_helpers import Outcome

class Vehicle(ModelBase):
    """
    A type of rocket e.g. F9 1.2, FH etc
    """
    name = sa.Column(sa.Text, nullable=False)

class FlightVehicle(ModelBase):
    """
    A specific combination of flight hardware for a launch. Used only once.
    """
    name = sa.Column(sa.Text, nullable=False)
    launch_id = sa.Column(sa.ForeignKey('launch.id', ondelete='CASCADE'))
    vehicle_id = sa.Column(sa.ForeignKey('vehicle.id'))

    launch = sa.orm.relationship('Launch')
    vehicle = sa.orm.relationship('Vehicle')
    boosters = sa.orm.relationship('Vehicle')
    upper_stages = sa.orm.relationship('Vehicle')

class Payload(ModelBase):
    name = sa.Column(sa.Text, nullable=False)
    customer = sa.Column(sa.Text)
    flight_vehicle_id = sa.Column(sa.ForeignKey('flightvehicle.id'), nullable=False)
    payload_type = sa.Column(sa.Enum('Primary', 'Secondary'), default='Primary')
    mass = sa.Column(sa.Float)
    target_orbit = sa.Column(sa.Text)
    deploy_outcome = sa.Column(sa.Enum(Outcome.options), default=Outcome.unknown.value)
    deploy_outcome_description = sa.Column(sa.Text)

    flight_vehicle = sa.orm.relationship('FlightVehicle')

class BoostStage(ModelBase):
    name = sa.Column(sa.Text, nullable=False)
    block = sa.Column(sa.Text)
    center_core = sa.Column(sa.Boolean)

class FlightVehicleBoostStage(ModelBase):
    boost_stage_id = sa.Column(sa.ForeignKey('booststage.id'), nullable=False)
    flight_vehicle_id = sa.Column(sa.ForeignKey('flightvehicle.id'), nullable=False)
    landing_legs = sa.Column(sa.Boolean, default=True)
    grid_fins = sa.Column(sa.Boolean, default=True)
    comments = sa.Column(sa.Text)

    boost_stage = sa.orm.relationship('BoostStage')
    flight_vehicle = sa.orm.relationship('FlightVehicle')
