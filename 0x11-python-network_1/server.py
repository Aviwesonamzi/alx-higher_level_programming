from flask import Flask, request

app = Flask(__name__)

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    return 'Your email is: {}'.format(email), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

