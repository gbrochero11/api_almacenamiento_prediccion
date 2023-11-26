from app import app
from app.utils.db import db

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug = True, host='0.0.0.0')