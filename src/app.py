from flask import Flask, request
import interactive_conditional_samples as ics

app = Flask(__name__)

@app.route('/',methods=['POST'])
def generate_data():
    request_data = request.get_json()
    textinput = request_data['input']

    return ics.interact_model(textinput)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
