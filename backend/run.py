from app import create_app

#create flask app
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)