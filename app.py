from flask import Flask, render_template, request, jsonify
import awsgi

app = Flask(__name__)


@app.route('/')
def contact():
    heading = "Connect With Me"
    return render_template('contact.html', heading=heading)


@app.route('/test')
def test():
    return "test"

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Handle the received data here (e.g., save it to a database, send an email, etc.)
    return jsonify(message=f'Thank you for your message, {name}!')


@app.route('/visitors')
def another_page():
    total_visitors = 100
    return render_template('viewer_count.html', total_visitors=total_visitors)


# if __name__ == '__main__':
#     app.run(debug=True)


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
