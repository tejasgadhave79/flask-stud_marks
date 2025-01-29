from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Example data: a list of dictionaries with names and marks
try:
    with open('api/std_marks.json') as f:
        marks_data = json.load(f)
except FileNotFoundError:
    marks_data = []

@app.route('/api', methods=['GET'])
def get_marks():
    # Retrieve the list of names from query parameters
    names = request.args.getlist('name')
    
    if not names:
        return jsonify({'error': 'No name parameters provided'}), 400

    # Retrieve the corresponding marks from the marks_data list
    marks = []
    for name in names:
        # Search the list for the matching name
        mark_entry = next((entry for entry in marks_data if entry['name'].lower() == name.lower()), None)
        if mark_entry is None:
            marks.append(None)  # If the name is not found, append None or a default value
        else:
            marks.append(mark_entry['marks'])
    
    # Return only the marks in a JSON response in the format you requested
    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)
