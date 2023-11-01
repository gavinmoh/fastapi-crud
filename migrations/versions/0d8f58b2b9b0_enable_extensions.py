"""Enable extensions

Revision ID: 0d8f58b2b9b0
Revises: 
Create Date: 2023-10-25 11:58:09.157788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d8f58b2b9b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS \"pgcrypto\";")


def downgrade() -> None:
    op.execute("DROP EXTENSION IF EXISTS \"pgcrypto\";")
