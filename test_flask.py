import json
import pytest
from flask import url_for
from app import app, db, Transaction


def test_method_get_response_405():
    response = app.test_client().get('/transaction')
    assert response.status_code == 405

def test_transaction_status_code_insert_body_clear():
    response = app.test_client().post(
        '/transaction',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400

def test_transaction_status_code_insert_body():
    response = app.test_client().post(
        '/transaction',
        data=json.dumps({
        "estabelecimento": "45.283.163/0001-69",
        "cliente": "094.214.930-01",
        "valor": 10.5,
        "descricao": "compra via Shipay, Mercado"
        }),
        content_type='application/json',
    )
    assert response.status_code == 201

    
def test_transaction_response_body():
    response = app.test_client().post(
        '/transaction',
        data=json.dumps({
        "estabelecimento": "45.283.163/0001-69",
        "cliente": "094.214.930-01",
        "valor": 10.5,
        "descricao": "compra via Shipay, Mercado"
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    response = {
            "aceito": True
        }
    assert data == response


def test_transaction_status_code_empty_field():
    response = app.test_client().post(
        '/transaction',
        data=json.dumps({
        "estabelecimento": "",
        "cliente": "094.214.930-01",
        "valor": 2.00,
        "descricao": "compra via Shipay, Mercado"
        }),
        content_type='application/json',
    )
    assert response.status_code == 400

def test_record_db():

    record_number = len(Transaction.query.filter_by(custumer="094.214.930-01").all())
    app.test_client().post(
        '/transaction',
        data=json.dumps({
        "estabelecimento": "45.283.163/0001-69",
        "cliente": "094.214.930-01",
        "valor": 10.5,
        "descricao": "compra via Shipay, Mercado"
        }),
        content_type='application/json',
    )
    recorded_number = len(Transaction.query.filter_by(custumer="094.214.930-01").all())
    last_record = Transaction.query.filter_by(id=recorded_number).all()
    db.session.delete(last_record[0])
    db.session.commit()

    assert record_number < recorded_number