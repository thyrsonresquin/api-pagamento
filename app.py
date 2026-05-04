from flask import Flask, jsonify, request

app = Flask(__name__)

# rota responsável por criar um pagamento pix
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()
    return jsonify({"message": "pagamento pix criado com sucesso", "data": data}), 201

# rota responsável por receber a confirmação de pagamento pix
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    data = request.get_json()
    return jsonify({"message": "confirmação de pagamento pix recebida", "data": data}), 201

# rota responsável por recuperar um pagamento pix
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return jsonify({"message": "pagamento pix recuperado com sucesso", "data": {"id": payment_id}}), 200

if __name__ == '__main__':
    app.run(debug=True)