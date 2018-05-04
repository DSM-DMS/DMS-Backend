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

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args()

    app.config['RUN_SETTING']['port'] = args.port or app.config['PORT']

    app.run(**app.config['RUN_SETTING'])
