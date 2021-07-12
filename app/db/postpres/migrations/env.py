import os.path
import pathlib
from logging.config import fileConfig

import yaml
from alembic import context
from alembic.config import Config
from sqlalchemy.ext.asyncio import create_async_engine

from app.db.postpres.base import Base

config: Config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata

file_path = pathlib.Path(__file__).parent.parent.parent.parent.parent
file_name = "config.yml"
with open(os.path.join(file_path, file_name)) as file:
    documents = yaml.full_load(file)
    print(documents)
    config.set_main_option("sqlalchemy.url", documents["db"]["postpres"]["url"])


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    engine = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        echo=True
    )

    def do_migrations(connection):
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

    async with engine.connect() as connection:
        await connection.run_sync(do_migrations)


# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     import asyncio
#     asyncio.run(run_migrations_online())
