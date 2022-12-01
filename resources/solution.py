from flask_restful import Resource, reqparse, abort
from models.solution import SolutionModel
from models.region import RegionModel
# from utils.common_utils import ParseResponse
import jsonify

class Solution(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('name', type=str, required=True, nullable=False,
                        help='This field cannot be left blank')
    parser.add_argument('poc', type=str, required=True, nullable=False,
                        help='Must enter the point of contact')
    parser.add_argument('location', type=str, default='Delhi')
    parser.add_argument('region_id', type=int, required=True)
    parser.add_argument('contact_number', type=int, required=False)


    def __init__(self):
        pass

    def get(self, name):
        solution = SolutionModel.search_by_name(name)
        if solution:
            return solution.to_json()
        return {'message': 'Solution does not exist'}, 404

    def post(self, name):

        if SolutionModel.search_by_name(name):
            return {'message': "Solution with name '{}' already exists.".format(name)}, 400
        data = Solution.parser.parse_args()
        if not RegionModel.get_by_id(data['region_id']):
            abort(400, message="region id is invalid")
        solution = SolutionModel(**data)

        try:
            solution.persist()
        except:
            return {"message": "An error occurred saving the solution."}, 500
        return solution.to_json(), 201

    def delete(self, name):

        Solution = SolutionModel.search_by_name(name)
        if Solution:
            Solution.delete()
        return {'message': "Solution '{}' deleted".format(name)}

    # def put(self, name):
    #     # Create or Update
    #     data = Solution.parser.parse_args()
    #     solution = SolutionModel.search_by_name(name)
    #     if solution:
    #         # ani_todo: only update allowed fields
    #         solution = SolutionModel()
    #     else:
    #         # ani_todo
    #         solution = SolutionModel()

    #     solution.persist()
    #     return {'message': "Solution '{}' creation/update successful".format(name)}

class SolutionList(Resource):
    def get(self):
        solutions = SolutionModel.query.all()
        if solutions:
            response = {'solutions': [solution.to_json() for solution in solutions]}
            return response
        return {'solutions' : []}
