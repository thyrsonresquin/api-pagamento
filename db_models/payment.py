from repository.database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(255), nullable=True)
    expiration_data = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Payment {self.id} - {self.value} - {self.paid} - {self.bank_payment_id} - {self.qr_code} - {self.expiration_data}>'