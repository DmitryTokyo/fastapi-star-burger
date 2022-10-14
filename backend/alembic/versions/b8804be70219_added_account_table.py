"""Added account table

Revision ID: b8804be70219
Revises: 
Create Date: 2022-10-14 11:58:40.024519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8804be70219'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('banner position', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_banner_banner position'), 'banner', ['banner position'], unique=False)
    op.create_index(op.f('ix_banner_id'), 'banner', ['id'], unique=False)
    op.create_index(op.f('ix_banner_title'), 'banner', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_banner_title'), table_name='banner')
    op.drop_index(op.f('ix_banner_id'), table_name='banner')
    op.drop_index(op.f('ix_banner_banner position'), table_name='banner')
    op.drop_table('banner')
    # ### end Alembic commands ###
