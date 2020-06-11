"""Application entry point."""
from application import create_app

app = create_app()

app.config['SECRET_KEY'] = 'any secret string'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
