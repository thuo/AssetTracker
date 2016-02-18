"""empty message

Revision ID: b2505975e152
Revises: None
Create Date: 2016-02-18 11:56:26.985000

"""

# revision identifiers, used by Alembic.
revision = 'b2505975e152'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignments',
    sa.Column('asset_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('set_return_date', sa.DATETIME(), nullable=True),
    sa.Column('actual_return_date', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], [u'asset.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], )
    )
    ### end Alembic commands ###