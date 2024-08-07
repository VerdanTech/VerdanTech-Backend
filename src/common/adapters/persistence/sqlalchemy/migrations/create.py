# Standard Library
import argparse
import os

# External Libraries
from alembic import command
from alembic.config import Config

# VerdanTech Source
from src import settings

# Find the directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))
config_directory = os.path.join(current_directory, "alembic.ini")
script_location = os.path.join(current_directory, "alembic/")

def create_migration(message: str):
    """
    Script to create migrations from the database tables.
    
    Args:
        message (str): the migration message to apply to the migration.
    """
    alembic_cfg = Config(config_directory)
    alembic_cfg.set_main_option("sqlalchemy.url", settings.POSTGRES_URI)
    alembic_cfg.set_main_option("script_location", script_location)
    command.revision(alembic_cfg, message=message, autogenerate=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create database migration")
    parser.add_argument("-m", "--message", type=str, required=True, help="Migration message")
    args = parser.parse_args()
    create_migration(args.message)