from argparse import ArgumentParser
import os

from flask import render_template

from app import app


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-p', '--port')

    args = parser.parse_args()

    if os.getenv('MYSQL_PW'):
        from utils import db_migrator

        db_migrator.migrate_posts()

    app.run(host=app.config['HOST'], port=int(args.port) if args.port else app.config['PORT'], debug=app.debug, threaded=True)
