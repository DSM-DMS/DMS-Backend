from server import app

if __name__ == '__main__':
    app.run(**app.config['RUN_SETTING'])