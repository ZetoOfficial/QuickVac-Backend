"""add vacancy skills

Revision ID: 1771f214a4d6
Revises: 2767b34e5815
Create Date: 2024-06-14 19:26:24.792778

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1771f214a4d6'
down_revision: Union[str, None] = '2767b34e5815'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'vacancy_skills',
        sa.Column('vacancy_id', sa.UUID(), nullable=False),
        sa.Column('skill_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ['skill_id'],
            ['skills.id'],
        ),
        sa.ForeignKeyConstraint(
            ['vacancy_id'],
            ['vacancies.id'],
        ),
        sa.PrimaryKeyConstraint('vacancy_id', 'skill_id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancy_skills')
    # ### end Alembic commands ###
