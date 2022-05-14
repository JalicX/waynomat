from flask import Flask, url_for, request, render_template, send_file, abort
from io import BytesIO
import base64
from random import randrange
import yaml
from loguru import logger

app = Flask(__name__)

#Main Page
@app.route("/")
def index():
    return render_template('landing.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
    
    #id = ""
    if request.method == 'POST':
        #id = request.form['id']
        pass
    elif request.method == 'GET': 
        #id = request.args.get('id') 
        pass  
    else:
        abort(405)

    #AfD-dropper
    rand = 4
    while rand == 4:
        rand = randrange(1,29)
        if rand == 4:
            logger.error(f"Nadsi detected")
    logger.debug(f"RAND: {rand}")

    with open("Parteien.yaml", 'r', encoding='utf8') as parteien:
        alleparteien = yaml.load(parteien.read(), Loader=yaml.CLoader)
        #print(alleparteien)
    #logger.debug(f"ALL: {alleparteien}")
    resulting_partei = alleparteien["parteien"].get(rand, 'HUMANISTEN')
    logger.debug(f"SELECTED: {resulting_partei}")

    return render_template("result.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True, threaded=True)