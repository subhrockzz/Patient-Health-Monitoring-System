import json
import random
import time
import asyncio
from datetime import datetime

from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator


@application.route('/')
def index():
    return render_template('ssh2.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        graph_data = open('example.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps({'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(y)})
                #var = f`var json_data = []; {json_data} return json_data ;` #f'data:{json_data}'
                yield f"data:{json_data}".join('\n\n') 
                time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
