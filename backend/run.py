from app import create_app
from flask_cors import CORS

#create flask app
app = create_app()

core = CORS(
    app,
    supports_credentials=True,
    allow_headers="*",
    expose_headers="*",
    origins="*"
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)