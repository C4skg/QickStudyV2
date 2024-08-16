from flask import session
from flask_migrate import Migrate, upgrade ,MigrateCommand
from flask_script import Manager
from api import create_app,db
from api.utils.user import generateSessionId

from api.models import (
    User,
    Logs,
    Posts,
    Comments,
    PostsCollection,
    Stars,
    Follows,
    PostsLabels,
    Labels
)

try:
    app = create_app('QickStudyV2',template_folder='api/templates')
except Exception as e:
    exit(e)

migrate = Migrate(app,db);
manager = Manager(app);

@app.before_request
def before_request():
    session_id = app.config['SESSION_ID'];
    if session.get(session_id):
        pass;
    else:
        session[session_id] = generateSessionId();

@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        User=User,
        Logs=Logs,
        Posts=Posts,
        Comments=Comments,
        PostsCollection=PostsCollection,
        PostsLabels=PostsLabels,
        Stars=Stars,
        Follows=Follows,
        Labels=Labels
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