"""primeira

Revision ID: 72c6865378c6
Revises: 
Create Date: 2024-08-22 10:42:00.371694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72c6865378c6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
                'pessoas',
                sa.Column('id', sa.Integer, primary_key=True),
                sa.Column('nome', sa.String(length=50), nullable=False),
                sa.Column('email', sa.String(length=50), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('pessoas')
