"""empty message

Revision ID: 32408eeecede
Revises: b2505975e152
Create Date: 2016-02-19 10:54:55.165000

"""

# revision identifiers, used by Alembic.
revision = '32408eeecede'
down_revision = 'b2505975e152'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('google_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('google_id', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('google_id')
    )
    op.add_column(u'user', sa.Column('profile_pic_url', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'profile_pic_url')
    op.drop_table('google_user')
    ### end Alembic commands ###