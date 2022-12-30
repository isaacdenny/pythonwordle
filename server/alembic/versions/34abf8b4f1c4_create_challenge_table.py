"""create_challenge_table

Revision ID: 34abf8b4f1c4
Revises: 545247292336
Create Date: 2022-12-29 17:27:40.146585

"""
import enum
from alembic import op
import sqlalchemy as sa

class ChallengeType(enum.Enum):
    normal: 1
    hard: 2
    special: 3
    deadly: 4

# revision identifiers, used by Alembic.
revision = '34abf8b4f1c4'
down_revision = '545247292336'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'challenge',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('type', sa.Enum(ChallengeType), nullable=False),
        sa.Column('provided_hint', sa.String(50), nullable=False),
        sa.Column('views', sa.Integer, nullable=False),
        sa.Column('fails', sa.Integer, nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('solved_by', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('solved_at', sa.DateTime, nullable=False),
        sa.Column('isPublished', sa.Boolean, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('challenge')
