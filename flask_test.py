from flask import Flask, request

from java.lang import System

app = Flask(__name__)

@app.route("/brython.js", methods=["GET"])
def brython3_js_module():
    return "".join(open("src/brython.js", 'r').readlines())

@app.route("/brython_stdlib.js", methods=["GET"])
def brython3_js_stdlib_modules():
    return "".join(open("src/brython_stdlib.js", 'r').readlines())

@app.route("/Lib/<path:subpath>", methods=["GET"])
def brython_libraries(subpath):
    return "".join(open("brython_libraries/Lib/"+subpath, 'r').readlines())

@app.route("/libs/<path:subpath>", methods=["GET"])
def brython_javascript_libraries(subpath):
    return "".join(open("brython_libraries/libs/"+subpath, 'r').readlines())



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        #print(request.data)
        System.out.println("%s" % request.data)
        return "Post request made\n"
    if request.method == "GET":
        return """<html>
<head>
<script src="/brython.js"></script>
</head>
<body onload="brython()">
<script type="text/python">
from browser import document
from browser.widgets.dialog import InfoDialog

def click(ev):
    InfoDialog("Hello", f"Hello, {document['zone'].value} !")

# bind event 'click' on button to function echo
document["echo"].bind("click", click)</script>
<input id="zone">
<button id="echo">click !</button>
</body>
</html>"""

#app.run(host="0.0.0.0", port=5000, debug=True)