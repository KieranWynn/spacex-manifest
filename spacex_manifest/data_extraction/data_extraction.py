import sqlalchemy as sa
from sqlalchemy import orm
from spacex_manifest import models

from typing import Iterable

def get_boosters(session: sa.orm.Session) -> Iterable[models.hardware.BoostStage]:
    return (result for result in session.query(models.hardware.BoostStage))
