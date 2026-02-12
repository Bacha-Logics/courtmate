"""add closed_at to cases

Revision ID: 1cee64b886fa
Revises: 568b093fb6ad
Create Date: 2026-02-09 12:50:04.733702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cee64b886fa'
down_revision: Union[str, Sequence[str], None] = '568b093fb6ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "cases",
        sa.Column("closed_at", sa.DateTime(), nullable=True)
    )


def downgrade():
    op.drop_column("cases", "closed_at")