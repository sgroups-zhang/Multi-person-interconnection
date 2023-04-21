from flask import Flask
import settings
from apps.user.view import user_bp

def create_app():
    app = Flask(__name__,template_folder="../templates")
    app.config.from_object(settings) # 添加配制
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
