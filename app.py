from flask import Flask, render_template, request
from pytube import YouTube
from tkinter import filedialog
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        # Open file dialog to choose download directory
        download_path = filedialog.askdirectory()

        # Check if user selected a directory
        if download_path:
            download_folder = os.path.join(download_path, 'downloads')
            os.makedirs(download_folder, exist_ok=True)  # Create the folder if it doesn't exist
            video.download(download_folder)
            return render_template('test.html')
            return 'Download completed successfully!'
           
        else:
            return 'No directory selected.'
    except Exception as e:
        return f'Error during download: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
