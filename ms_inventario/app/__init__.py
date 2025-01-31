from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


#patron saga
#orquestador 
#coreografia
#con orchesta hay delay, esto se soluciona con redis (db que actua como cache(?)

migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()

def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    f.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from .resources import stock
    app.register_blueprint(stock, url_prefix='/api/v1/stock')

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
            'db' : db
            }
    
    return app



"""
para usar con postman
[
    {
        "cantidad": 100,
        "entrada_salida": 1,
        "fecha_transaccion": "2024-11-04T00:47:11.169077",
        "id": 1,
        "producto_id": 1
    }
]
"""