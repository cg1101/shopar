"""empty message

Revision ID: d720c12b6d88
Revises: 
Create Date: 2020-04-04 12:34:46.289977

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd720c12b6d88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('merchandises',
    sa.Column('merchanise_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('picture', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('merchanise_id'),
    mysql_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('merchandises')
    # ### end Alembic commands ###
