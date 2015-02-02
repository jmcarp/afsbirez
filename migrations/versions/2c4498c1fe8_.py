"""empty message

Revision ID: 2c4498c1fe8
Revises: 2362a05f722a
Create Date: 2015-02-02 15:16:34.009127

"""

# revision identifiers, used by Alembic.
revision = '2c4498c1fe8'
down_revision = '2362a05f722a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('references', sa.Column('topic_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'references', 'topics', ['topic_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'references', type_='foreignkey')
    op.drop_column('references', 'topic_id')
    ### end Alembic commands ###
