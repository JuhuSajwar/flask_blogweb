from flask import Flask

app= Flask(__name__)

from blog_app.core.views import core
app.register_blueprint(core)