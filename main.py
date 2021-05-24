from flask import Flask
from flask_restful import Api
from resource.video import Video

app = Flask(__name__)
api = Api(app)


api.add_resource(Video, "/video/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
