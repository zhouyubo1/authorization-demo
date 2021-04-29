from app import create_app

from flask_script import Manager, Server

app = create_app()

app.debug = True

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=app.config.port))

if __name__ == '__main__':
    print(app.url_map)
    manager.run()