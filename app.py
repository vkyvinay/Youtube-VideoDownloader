from flask import *
from pytube import YouTube

app  = Flask(__name__)
app.secret_key="DemoString"

@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        link = YouTube(request.form.get('url'))
        download(link)
    return render_template('index.html')

def download(link):
    video = link.streams.first()
    video.download("link")

if __name__=="__main__":
    app.run(debug=True)