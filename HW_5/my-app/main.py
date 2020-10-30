from app import app

app.config.update(
    
    DEBUG=True,
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key",
)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True)