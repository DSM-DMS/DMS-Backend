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
    if os.getenv('MYSQL_PW'):
        from utils import db_migrator

        db_migrator.migrate_posts()

    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)
