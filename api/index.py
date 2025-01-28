# from flask import Flask, request, jsonify
import json

# app = Flask(__name__)

# Example data: a dictionary mapping names to marks
with open('api/std_marks.json') as f:
    marks_data = json.load(f)

# @app.route('/api', methods=['GET'])
# def get_marks():
#     # Retrieve the list of names from query parameters
#     names = request.args.getlist('name')
    
#     # Retrieve the corresponding marks from the marks_data dictionary
#     marks = [marks_data.get(name.lower(), None) for name in names]
    
#     # Return the marks in a JSON response
#     return jsonify({'marks': marks})

# if __name__ == '__main__':
#     app.run(debug=True)
print(marks_data)