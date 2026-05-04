# Pagamento PIX
Este é um exemplo de aplicação Flask para simular um sistema de pagamento PIX. A aplicação possui três rotas principais:

1. **Criar Pagamento PIX**: Rota `POST /payments/pix` para criar um novo pagamento PIX.
2. **Confirmação de Pagamento PIX**: Rota `POST /payments/pix/confirmation` para receber a confirmação de um pagamento PIX (simulando um webhook).
3. **Recuperar Pagamento PIX**: Rota `GET /payments/pix/<payment_id>` para recuperar os detalhes de um pagamento PIX específico.


