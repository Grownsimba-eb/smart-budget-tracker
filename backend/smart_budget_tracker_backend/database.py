from sqlalchemy.orm import declarative_base

Base = declarative_base()

# If you also define engine here, fine — Alembic uses only Base.metadata.
