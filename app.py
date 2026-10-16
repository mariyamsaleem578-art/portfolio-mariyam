from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    message_sent = False
    return render_template('index.html', message_sent=message_sent)

@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"New Message: Name={name} | Email={email} | Message={message}")
    
    # form submit ke baad wapis home page pe "Sent" msg ke sath
    return render_template('index.html', message_sent=True)

if __name__ == '__main__':
    app.run(debug=True)