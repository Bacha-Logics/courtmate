"""add created_at to cases

Revision ID: 568b093fb6ad
Revises: 27ae359c374b
Create Date: 2026-01-30
"""

from alembic import op
import sqlalchemy as sa
from datetime import datetime

# 🔑 REQUIRED BY ALEMBIC
revision = "568b093fb6ad"
down_revision = "27ae359c374b"
branch_labels = None
depends_on = None


def upgrade():
    # 1️⃣ Add column as nullable first
    op.add_column(
        "cases",
        sa.Column("created_at", sa.DateTime(), nullable=True)
    )

    # 2️⃣ Backfill existing rows
    op.execute(
        "UPDATE cases SET created_at = NOW() WHERE created_at IS NULL"
    )

    # 3️⃣ Enforce NOT NULL
    op.alter_column(
        "cases",
        "created_at",
        nullable=False
    )


def downgrade():
    op.drop_column("cases", "created_at")
