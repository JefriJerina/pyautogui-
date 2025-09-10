from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/retrain', methods=['POST'])
def retrain():
    data = request.get_json()
    model_id = data.get('modelId', 'unknown_model')
    training_data = data.get('trainingData', 'none')

    # Here you can add your retraining logic
    print(f"Retraining model {model_id} with data: {training_data}")

    return jsonify({
        "status": "success",
        "message": f"Retraining started for {model_id} with {training_data} data"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
