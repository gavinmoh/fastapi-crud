"""Create books table

Revision ID: 6e99a2af0456
Revises: 0d8f58b2b9b0
Create Date: 2023-10-25 12:16:23.537019

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Text, TIMESTAMP


# revision identifiers, used by Alembic.
revision: str = '6e99a2af0456'
down_revision: Union[str, None] = '0d8f58b2b9b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books",
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()),
        Column("title", String),
        Column("description", Text),
        Column("created_at", TIMESTAMP, server_default=func.now()),
        Column("updated_at", TIMESTAMP, server_default=func.now(), onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table("books")
