"""add lxc_metrics table

Revision ID: 9452170fda2c
Revises: 0ef28e556491
Create Date: 2026-05-20 19:34:52.036904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9452170fda2c'
down_revision: Union[str, Sequence[str], None] = '0ef28e556491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'lxc_metrics',
        sa.Column('id', sa.BigInteger(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('status', sa.String()),
        sa.Column('cpu', sa.Float()),
        sa.Column('memory', sa.BigInteger()),
        sa.Column('recorded_at', sa.DateTime()),
    )

def downgrade() -> None:
    op.drop_table('lxc_metrics')
