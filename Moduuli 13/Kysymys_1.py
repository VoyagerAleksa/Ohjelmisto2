from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

@app.route("/alkuluku/<int:number>")
def prime_route(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })

@app.route("/")
def home():
    return "Server is running"

if __name__ == "__main__":
    app.run(port=3000)