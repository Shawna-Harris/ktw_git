from website import create_app


app = create_app()
# only if run file run webserver
if __name__ == '__main__':
    app.run(debug=True)
