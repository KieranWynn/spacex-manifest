import logging
import contextlib
import sqlalchemy as sa
import sqlalchemy.orm
import sqlalchemy.exc

from ..models.base import Base

logger = logging.getLogger(__name__)

class Database(object):
    def __init__(self, db_connection_string, drop_and_recreate_schema=False):
        self.connection_string = db_connection_string
        self.smash_schema = drop_and_recreate_schema
        self.setup()

    def setup(self):
        logger.debug('Creating engine')
        self.engine = sa.create_engine(self.connection_string, echo=True)
        self.initialise()
        self.session_maker = sa.orm.sessionmaker(bind=self.engine)

    @staticmethod
    def drop_all(engine):
        logger.debug('Dropping schema')
        Base.metadata.drop_all(engine)

    @staticmethod
    def create_all(engine):
        logger.debug('Creating schema')
        Base.metadata.create_all(engine)

    def initialise(self):
        if self.smash_schema:
            self.drop_all(self.engine)
            self.create_all(self.engine)

    @property
    @contextlib.contextmanager
    def managed_session(self) -> sa.orm.Session:
        logger.debug('Creating session')
        session = self.session_maker()
        try:
            yield session
        except sa.exc.SQLAlchemyError:
            session.rollback()
            logger.error("Error during database session.")
            logger.debug('Rolling back session')
            raise
        logger.debug('Commiting session')
        session.commit()
