
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import BIT, VARCHAR, INTEGER as INT

metadata = sa.MetaData()


##########################################################################

t_merchandises = sa.Table('merchandises', metadata,
    sa.Column('merchanise_id', INT(11), primary_key=True, autoincrement=True),
    sa.Column('name', VARCHAR(255), nullable=True),
    sa.Column('description', VARCHAR(255), nullable=True),
    sa.Column('picture', VARCHAR(255), nullable=True),
    mysql_engine='InnoDB',
    mysql_charset='utf8',
)

t_tenants = sa.Table('tenants', metadata,
    sa.Column('tenant_id', INT(11), primary_key=True, autoincrement=True),
    sa.Column('name', VARCHAR(255), nullable=True),
    sa.Column('description', VARCHAR(255), nullable=True),
    sa.Column('admin_email', VARCHAR(255), nullable=True),
    mysql_engine='InnoDB',
    mysql_charset='utf8',
)


##########################################################################


__all__ = [name for name in locals().keys()
        if name.startswith('t_') or name.startswith('j_')]
__all__.insert(0, 'metadata')
