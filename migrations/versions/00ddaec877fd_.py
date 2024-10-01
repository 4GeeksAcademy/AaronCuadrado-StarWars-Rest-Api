"""empty message

Revision ID: 00ddaec877fd
Revises: a5cffa318ac2
Create Date: 2024-10-01 19:24:46.680403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00ddaec877fd'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=100), nullable=True),
    sa.Column('eye_color', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('birth_year', sa.String(length=100), nullable=False),
    sa.Column('skin_color', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###
