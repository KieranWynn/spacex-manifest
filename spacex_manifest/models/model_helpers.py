from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects import postgresql
import uuid
import enum


from typing import Optional, Union

class Outcome(enum.Enum):
    unknown = 'Unknown'
    success = 'Success'
    partial_success = 'Partial Success'
    failure = 'Failure'

    @classmethod
    def options(cls):
        return [a.value for a in cls]

class UUID(TypeDecorator):
    """DB Platform-independent UUID type.

    Uses Postgresql's UUID type, otherwise uses CHAR(32), storing as stringified hex values.

    To set a meaningly server default, use:
      server_default=sa.text('uuid_generate_v4()')

    """
    impl = CHAR
    python_type = uuid.UUID

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(postgresql.UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value: Union[uuid.UUID, str, None], dialect) -> Optional[str]:
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if isinstance(value, uuid.UUID):
                # hexstring
                return '{:32x}'.format(value.int)
            else:
                return '{:32x}'.format(uuid.UUID(value).int)

    def bind_processor(self, dialect):
        return lambda val: self.process_bind_param(val, dialect)

    def process_result_value(self, value: Union[uuid.UUID, str, None], dialect) -> Optional[uuid.UUID]:
        if value is None:
            return value
        elif isinstance(value, uuid.UUID):
            return value
        else:
            return uuid.UUID(value)
