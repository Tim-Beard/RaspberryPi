'''
Code created by Matt Richardson 
for details, visit: <a href="http://mattrichardson.com/Raspberry-Pi-Flask/index.html"> http://mattrichardson.com/Raspberry-Pi-Flask/inde...</a>
'''

from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)