from app_v1 import app as app_v1
from app_v2 import app as app_v2


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

    app_v1.run(host=app_v1.config['HOST'], port=int(args.port) if args.port else app_v1.config['PORT'], debug=app_v1.debug, threaded=True)
    # app_v2.run(host=app_v2.config['HOST'], port=int(args.port) if args.port else app_v2.config['PORT'], debug=app_v2.debug, threaded=True)
