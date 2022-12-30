"""create user table

Revision ID: 545247292336
Revises: 
Create Date: 2022-12-28 02:57:03.515102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '545247292336'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('total_solved', sa.Integer, nullable=False),
        sa.Column('total_failed', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user')
