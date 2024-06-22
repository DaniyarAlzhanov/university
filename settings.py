"""File with settings and cofigs for the project"""

from envparse import Env


env = Env()

REAL_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default='postgresql+asyncpg://postgres:postgres@localhost:54320/postgres'
) # connect string for the database