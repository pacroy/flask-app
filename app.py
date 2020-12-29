from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26383-1381845104-25.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25329-1381845415-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25158-1381844793-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-23859-1381845509-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19708-1381845008-7.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19645-1381845207-5.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-18774-1381844645-6.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-11864-1381846346-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3391-1381844336-26.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
