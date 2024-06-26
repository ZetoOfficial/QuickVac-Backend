"""Initial migration

Revision ID: 2767b34e5815
Revises: 
Create Date: 2024-06-14 18:57:53.353457

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2767b34e5815'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'companies',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('address', sa.String(length=255), nullable=True),
        sa.Column('website', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'skills',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'vacancies',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('salary_amount', sa.DECIMAL(precision=10, scale=2), nullable=True),
        sa.Column('salary_currency', sa.String(length=10), nullable=True),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.Column('status', sa.Enum('open', 'closed', 'pending', name='vacancystatus'), nullable=False),
        sa.Column(
            'direction',
            sa.Enum(
                'development',
                'sales',
                'customer_service',
                'marketing',
                'hr',
                'product_management',
                'business_development',
                'data_analytics',
                name='direction',
            ),
            nullable=False,
        ),
        sa.Column(
            'work_type',
            sa.Enum('full_time', 'part_time', 'contract', 'freelance', 'internship', name='worktype'),
            nullable=False,
        ),
        sa.Column(
            'experience_level', sa.Enum('junior', 'middle', 'senior', 'lead', name='experiencelevel'), nullable=False
        ),
        sa.Column(
            'employment_type',
            sa.Enum('permanent', 'temporary', 'contract', 'internship', name='employmenttype'),
            nullable=False,
        ),
        sa.Column(
            'education_level',
            sa.Enum('high_school', 'bachelor', 'master', 'phd', 'no_degree', name='educationlevel'),
            nullable=False,
        ),
        sa.Column('company_id', sa.UUID(), nullable=True),
        sa.Column('posted_date', sa.Date(), nullable=False),
        sa.Column('closing_date', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(
            ['company_id'],
            ['companies.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancies')
    op.drop_table('skills')
    op.drop_table('companies')
    # ### end Alembic commands ###
