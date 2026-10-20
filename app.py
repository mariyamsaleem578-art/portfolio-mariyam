from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    print(request.form)
    return "Message Sent! I will reply soon."

if __name__ == '__main__':
    app.run(debug=True, port=5000)