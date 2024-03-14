from api import create_app

try:
    app = create_app()
except Exception as e:
    exit(e)

if __name__ == '__main__':
    app.run();