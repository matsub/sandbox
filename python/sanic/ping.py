from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/ping")
async def index(request):
    return json({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
