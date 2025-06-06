"""Nova estrutura do banco com mais informações

Revision ID: 230b59a8a4d0
Revises: 
Create Date: 2025-05-05 13:35:45.557578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '230b59a8a4d0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('placa', sa.String(), nullable=False),
    sa.Column('chassi', sa.String(), nullable=False),
    sa.Column('marca', sa.String(), nullable=False),
    sa.Column('modelo', sa.String(), nullable=False),
    sa.Column('ano', sa.Integer(), nullable=False),
    sa.Column('cor', sa.String(), nullable=True),
    sa.Column('cilindros', sa.Integer(), nullable=True),
    sa.Column('combustivel', sa.String(), nullable=False),
    sa.Column('categoria', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chassi'),
    sa.UniqueConstraint('placa')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('car_id')
    )
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('cep', sa.String(), nullable=True),
    sa.Column('rua', sa.String(), nullable=True),
    sa.Column('numero', sa.String(), nullable=True),
    sa.Column('complemento', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.Column('estado', sa.String(), nullable=True),
    sa.Column('pais', sa.String(), nullable=True),
    sa.Column('cpf', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    op.drop_table('user_cars')
    op.drop_table('users')
    op.drop_table('cars')
    # ### end Alembic commands ###
