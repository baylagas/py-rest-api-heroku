from flask_restful import Resource, reqparse
from logic.video_logic import VideoLogic


class Video(Resource):
    def __init__(self):
        self.video_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("name", type=str, help="name of the video", required=True)
        args.add_argument("likes", type=int, help="likes of the video", required=True)
        args.add_argument("views", type=int, help="views of the video", required=True)
        return args

    def get(self, id):
        logic = VideoLogic()
        result = logic.getVideoById(id)
        return result, 200

    def put(self, id):
        args = self.video_put_args.parse_args()
        logic = VideoLogic()
        rowsAffected = logic.insertVideo(args)
        return rowsAffected, 201

    def patch(self, id):
        args = self.video_put_args.parse_args()
        logic = VideoLogic()
        rowsAffected = logic.updateVideo(id, args)
        return rowsAffected, 200

    def delete(self, id):
        logic = VideoLogic()
        rowsAffected = logic.deleteVideo(id)
        return rowsAffected, 200
