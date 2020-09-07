from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    establishment = db.Column(db.String, nullable=False)
    custumer = db.Column(db.String, nullable=False)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)



@app.route('/transaction', methods=['POST'])
def transaction():
    json = request.json

    verify_body = True
    if not json:
        verify_body = False
    for key in json:
        response = json[key]
        if not response:
            verify_body = False

    if verify_body:
        transaction = Transaction(
            establishment=json["estabelecimento"],
            custumer=json["cliente"],
            value=json["valor"],
            description=json["descricao"]
        )
        db.session.add(transaction)
        db.session.commit()

        msg = {
            "aceito": True
        }
        return jsonify(msg), 201
    else:
        msg = {
            "error": "body or field empty"
        }
        return jsonify(msg), 400


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'foo': 'bar'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')