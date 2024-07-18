from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == "__main__":
    app.run(port = 5000,debug = True)
