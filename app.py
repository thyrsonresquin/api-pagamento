from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

# rota responsável por criar um pagamento pix
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()
    
    #validacoes
    if 'value' not in data:
        return jsonify({"message": "campo 'value' é obrigatório"}), 400
    
    # calculando a data de expiração do pagamento pix (30 minutos a partir do momento da criação)
    expiration_date = datetime.now() + timedelta(minutes=30)

    # criando um novo pagamento pix e salvando no banco de dados
    new_payment = Payment(
        value=data['value'],
        expiration_date=expiration_date
    )
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "pagamento pix criado com sucesso",
                    'payment_id': new_payment.to_dict()['id'],
                    "data": data, "expiration_date": expiration_date}), 201

# rota responsável por receber a confirmação de pagamento pix (webhook)
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