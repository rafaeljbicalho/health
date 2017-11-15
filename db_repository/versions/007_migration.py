from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('user_id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=20)),
    Column('password', String(length=250)),
    Column('cpf', Integer),
    Column('sexo', String(length=250)),
    Column('data_nascimento', String(length=250)),
    Column('peso', String(length=250)),
    Column('altura', String(length=250)),
    Column('registered_on', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['altura'].create()
    post_meta.tables['user'].columns['data_nascimento'].create()
    post_meta.tables['user'].columns['peso'].create()
    post_meta.tables['user'].columns['sexo'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['altura'].drop()
    post_meta.tables['user'].columns['data_nascimento'].drop()
    post_meta.tables['user'].columns['peso'].drop()
    post_meta.tables['user'].columns['sexo'].drop()
