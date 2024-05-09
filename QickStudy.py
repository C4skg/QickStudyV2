from flask_migrate import Migrate, upgrade ,MigrateCommand
from flask_script import Manager
from api import create_app,db

from api.models import (
    User,
    Logs,
    Posts,
    Comments,
    PostsCollection,
    Stars,
    Follows
)

try:
    app = create_app()
except Exception as e:
    exit(e)

migrate = Migrate(app,db);
manager = Manager(app);

@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        User=User,
        Logs=Logs,
        Posts=Posts,
        Comments=Comments,
        PostsCollection=PostsCollection,
        Stars=Stars,
        Follows=Follows
    )

manager.add_command('db',MigrateCommand);

@manager.command
def deploy():
    from api.models import insertAdmin

    try:
        upgrade();
    except:
        pass;
    insertAdmin();


if __name__ == '__main__':
    manager.run()