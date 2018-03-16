from app import app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()

    import os
    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable !!')

    # if os.getenv('MYSQL_PW'):
    #     from utils import db_migrator
    #
    #     db_migrator.migrate_posts()

    from utils.schedulers import apply_status_cleaner
    apply_status_cleaner.run()

    app.run(host=app.config['HOST'], port=int(args.port) if args.port else app.config['PORT'], debug=app.debug, threaded=True)
