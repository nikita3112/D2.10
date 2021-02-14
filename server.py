import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://7739534769b041cdadd08ce9cb740c59@o517702.ingest.sentry.io/5625856",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/success')
def index():
    return "200 OK"

@app.route('/fail')
def index():
    raise RuntimeError("There is a error!")
    return

app.run(host='localhost', port=8080)