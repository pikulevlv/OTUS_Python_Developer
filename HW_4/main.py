from app import app

app.config.update(
    DEBUG=True,
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
)


if __name__ == '__main__':
    app.run(debug=True)