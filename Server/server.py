from multiprocessing import Process

from app import app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()

    import os
    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    # from utils.meal_parser import parse
    # parse()

    # from utils.db_migrator import migration
    # migration()

    from utils.influx_setup import setup
    Process(target=setup).start()

    from utils import extension_apply_cleaner
    Process(target=extension_apply_cleaner.run).start()

    app.run(host=app.config['HOST'], port=int(args.port) if args.port else app.config['PORT'], debug=app.debug, threaded=True)
