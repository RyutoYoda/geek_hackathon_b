from flask import Flask
from flask_cors import CORS
import os



def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    CORS(app)
    app.json.ensure_ascii=False
    
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path,"flaskr.sqlite")
    )
    if test_config is None:
        app.config.from_pyfile("config.py",silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass
    
    @app.route("/")
    def hello():
        return "Hello, World!"
    from feature import db
    db.init_app(app)

    from feature import auth
    app.register_blueprint(auth.bp)

    
    return app