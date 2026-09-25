from flask import Flask
from compliance_rewriter import bp
app = Flask(__name__); app.register_blueprint(bp)
