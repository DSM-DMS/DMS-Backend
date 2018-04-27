from multiprocessing import Process
import os

from app import app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args()

    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    from utils import extension_apply_cleaner
    Process(target=extension_apply_cleaner.run).start()

    app.run(host=app.config['HOST'], port=args.port or app.config['PORT'], debug=app.debug, threaded=True)
