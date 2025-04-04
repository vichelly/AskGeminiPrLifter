from flask import Flask
from app.main_controller import main_controller 

app = Flask(__name__)
app.register_blueprint(main_controller)

if __name__ == '__main__':
    app.run(debug=True)
