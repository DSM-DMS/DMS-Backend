from datetime import datetime, timedelta
import os

from app import create_app
from config.production import ProductionConfig


if __name__ == '__main__':
    app = create_app(ProductionConfig)

    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    app.run(**app.config['RUN_SETTING'])
