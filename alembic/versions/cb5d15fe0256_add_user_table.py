"""Add user table

Revision ID: cb5d15fe0256
Revises: 
Create Date: 2024-09-22 22:55:58.695990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cb5d15fe0256'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_telegram_id', sa.Integer, unique=True, nullable=False),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('locale', sa.String(255)),
    )

def downgrade() -> None:
    op.drop_table('user')
