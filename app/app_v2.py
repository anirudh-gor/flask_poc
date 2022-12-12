from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.solution import Solution, SolutionList

# app and db setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flask_poc:password@localhost:5432/flask_db"
app.config["SECRET_KEY"] = "secret_key101"

CORS(app, origins="http://localhost:8000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True, intercept_exceptions=False)

# csrf = CSRFProtect(app)

@app.before_first_request
def create_tables():
    from app.db import db
    db.init_app(app)
    db.create_all()

# @app.before_request
# def pre_request_handling():
#     app.logger.info("pre request proc 1")

# @app.before_request
# def pre_request_handling_v2():
#     app.logger.info("pre request proc 2")

@app.after_request
def post_request_handling(ret):
    app.logger.info("post request proc")
    app.logger.info("post request proc 2")
    return ret

# Api resource setup
api = Api(app)
api.add_resource(SolutionList, '/solutions')
api.add_resource(Solution, '/solution/<string:name>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
