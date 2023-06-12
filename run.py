from flaskblog import app, db #will import from init file

if __name__ == '__main__': #this conditional is only true if we run the scrit directly
    with app.app_context():
        db.create_all()

    app.run(debug=True)