from flask import Flask, render_template, request, jsonify
import fuzzy_module  # Import your fuzzy logic module or define functions here

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
         # Get data from the form
        input_data = {
            'temperature': float(request.form['inputTemperature']),
            'headache': float(request.form['inputHeadacheLevel']),
            'eyepain': float(request.form['inputEyepainLevel']),
            'musclejointpain': float(request.form['inputMuscleJointPainLevel']),
            'nausea': float(request.form['inputNauseaLevel']),
            'vomiting': request.form.get('inputVomiting') == 'yes',
            'swollenglands': request.form.get('inputSwollenGland') == 'yes',
            'rash': request.form.get('inputRash') == 'yes',
        }

        # Call the fuzzy logic function
        result = fuzzy_module.perform_fuzzy_logic(**input_data)

        # Return the result as JSON
        return jsonify({'result': result})
    
    # Render the HTML template on GET request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)