from flask import Flask, request, abort

app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return 'Webhooks with Python'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"
    else:
        print('error')
        abort(400)

if __name__ == '__main__':
    app.run(port=5000)

