from app import create_app
from dotenv import load_env

app = create_app()

load_env()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


