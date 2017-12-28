import os
import unittest2 as ut

from app import app
from utils import db_migrator

if __name__ == '__main__':
    if app.config['TEST']:
        all_tests = ut.TestLoader().discover('tests', pattern='*.py')
        ut.TextTestRunner().run(all_tests)
        exit()
    else:
        if os.getenv('MYSQL_PW'):
            db_migrator.migrate_posts()

        app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug)

    # app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug)
