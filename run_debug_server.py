from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(
        port=8000, 
        debug=True, 
        host='0.0.0.0', 
        ssl_context=('keys/cert.pem', 'keys/key.pem')
    )