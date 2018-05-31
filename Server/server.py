from datetime import datetime, timedelta
from multiprocessing import Process
import os

from app import create_app
from config.dev import DevConfig
from config.production import ProductionConfig


if __name__ == '__main__':
    app = create_app(ProductionConfig)

    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    from utils import extension_apply_cleaner
    Process(target=extension_apply_cleaner.run).start()

    from utils.meal_parser import parse

    now = datetime.now()
    parse(now.year, now.month)

    a_month_after = now + timedelta(days=30)
    parse(a_month_after.year, a_month_after.month)

    app.run(**app.config['RUN_SETTING'])
