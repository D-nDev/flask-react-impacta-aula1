from flask import Flask, jsonify, request, render_template, make_response

app = Flask(__name__, static_url_path='',
            static_folder='static', template_folder='templates')


@app.route('/calc', methods=['POST'])
def controller_responde_template():
    data = request.json

    val1 = data['value1']
    val2 = data['value2']
    op = data['operation']

    if(not val1 or not val2 or not op):
        return "erro"

    if(op == "plus"):
        res = make_response(jsonify({"result": val1 + val2}), 200)
        return res
    elif(op == "minus"):
        res = make_response(jsonify({"result": val1 - val2}), 200)
        return res
    elif(op == "multiply"):
        res = make_response(jsonify({"result": val1 * val2}), 200)
        return res
    elif(op == "division"):
        res = make_response(jsonify({"result": val1 / val2}), 200)
        return res


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
