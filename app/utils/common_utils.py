import jsonify

class ParseResponse():
    def parse_solution(solution):
        return jsonify(solution)
    
    def parse_solutions(solutions):
        [ParseResponse.parse_solution(solution) for solution in solutions]
    
    def parse_region(region):
        return jsonify(region)
    
    def parse_regions(regions):
        return [ParseResponse.parse_region(region) for region in regions]
