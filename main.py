import flask

app = flask.Flask('UTN_Server')

@app.route('/',methods=['GET'])
def home():
    return flask.render_template('home.html')

@app.route('/informe',methods=['GET'])
def infrome():
    return flask.render_template('DataSheet.html')

@app.route('/datasheet',methods=['GET'])
def datasheet():
    return flask.send_file(path_or_file='./Electronics_Datasheet_Example.pdf',download_name='Datasheet.pdf')

if __name__ == '__main__':
    app.run(port=80,debug=True,host='localhost')