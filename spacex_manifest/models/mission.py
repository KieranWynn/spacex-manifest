import sqlalchemy as sa
from sqlalchemy import orm

from .base import ModelBase
from .model_helpers import Outcome

class OutcomeMixin(object):
    outcome = sa.Column(sa.Enum(Outcome))
    outcome_description = sa.Column(sa.Text)

    @property
    def successful(self):
        return self.outcome == Outcome.success.value

class StageFlightMixin(object):
    ascent_outcome = sa.Column(sa.Enum(Outcome.options), default=Outcome.unknown.value)
    ascent_outcome_description = sa.Column(sa.Text)

    descent_attempted = sa.Column(sa.Boolean, default=True)
    descent_outcome = sa.Column(sa.Enum(Outcome.options), default=Outcome.unknown.value)
    descent_outcome_description = sa.Column(sa.Text)

    landing_attempted = sa.Column(sa.Boolean, default=True)
    landing_outcome = sa.Column(sa.Enum(Outcome.options), default=Outcome.unknown.value)
    landing_outcome_description = sa.Column(sa.Text)
    landing_pad_id = sa.Column(sa.ForeignKey('landingpad.id'))
    landing_location_lattitude = sa.Column(sa.Float)
    landing_location_longitude = sa.Column(sa.Float)

    landing_pad = sa.orm.relationship('LandingPad')

class Mission(OutcomeMixin, ModelBase):
    name = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text)
    customer = sa.Column(sa.Text)

class Flight(OutcomeMixin, ModelBase):
    mission_id = sa.Column(sa.ForeignKey('mission.id', ondelete='CASCADE'))
    launch_pad_id = sa.Column(sa.ForeignKey('launchpad.id'), nullable=False)
    launch_datetime = sa.Column(sa.DateTime, nullable=False)

    mission = sa.orm.relationship('Mission')
    launch_pad = sa.orm.relationship('LaunchPad')

class BoostStageFlight(StageFlightMixin, ModelBase):
    flight_vehicle_boost_stage_id = sa.Column(sa.ForeignKey('flightvehiclebooststage.id'), nullable=False)
    boostback = sa.Column(sa.Boolean, default=False)
    rtls = sa.Column(sa.Boolean, default=False)

    flight_vehicle_boost_stage = sa.orm.relationship('FlightVehicleBoostStage')

