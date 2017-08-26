import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from .model_helpers import UUID

Base = declarative_base()


class ModelBase(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = sa.Column(UUID, nullable=False, primary_key=True, server_default=sa.text('uuid_generate_v4()'))
