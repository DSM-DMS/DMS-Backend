from argparse import ArgumentParser
import os
import unittest2 as ut

from app import app

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--travis', required=False)
    args = parser.parse_args()

    if app.config['TEST']:
        all_tests = ut.TestLoader().discover('tests', '*.py')
        ut.TextTestRunner().run(all_tests)
    else:
        if os.getenv('MYSQL_PW'):
            from utils import db_migrator

            db_migrator.migrate_posts()

    if not args.travis:
        app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)
