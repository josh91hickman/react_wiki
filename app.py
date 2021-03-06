import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='client/build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if(path == ""):
        return send_from_directory('client/build', 'index.html')
    else:
        if(os.path.exists("client/build/" + path)):
            return send_from_directory('client/build', path)
        else:
            return send_from_directory('client/build', 'index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000, threaded=True)