import os

from app import app

if __name__ == '__main__':
    if os.getenv('MYSQL_PW'):
        from utils import db_migrator

        db_migrator.migrate_posts()

    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)
