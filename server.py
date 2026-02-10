from flask_app import app
from flask_app.controllers import routes
from flask_app.controllers import splash_page

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5050)
