"""pokemons table

Revision ID: 92efd96fe4b2
Revises: 
Create Date: 2024-02-21 13:15:00.178177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, VARCHAR, Text


from app.config.settings import settings


# revision identifiers, used by Alembic.
revision: str = '92efd96fe4b2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        settings.table_name,
        Column('id', Integer, primary_key=True, index=True, autoincrement=True),
        Column('name', VARCHAR(50), index=True),
        Column('image', Text),
        Column('type', VARCHAR(50))
    )


def downgrade() -> None:
    pass
