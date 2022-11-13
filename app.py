templates = [
    {
        "inputs":10,
        "category":"Sports",
        "word":"BasketBall"
    },
    {
        "inputs":6,
        "category":"European Country Name",
        "word":"France"
    },

]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonif({
        "status":"success",
        "word": random.choice(templates)
    })