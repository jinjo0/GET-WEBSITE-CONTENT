from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch_content():
    url = request.form['url']
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        content = response.text
        return render_template('content.html', content=content)
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching content: {str(e)}"
        return render_template('error.html', error_message=error_message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


