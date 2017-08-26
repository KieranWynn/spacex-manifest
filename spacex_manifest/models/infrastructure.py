import sqlalchemy as sa
from sqlalchemy import orm

from .base import ModelBase

class LaunchPad(ModelBase):
    name = sa.Column(sa.Text, nullable=False)
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)

class LandingPad(ModelBase):
    name = sa.Column(sa.Text, nullable=False)
