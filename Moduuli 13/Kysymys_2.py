from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/kenttä/<icao>")
def get_airport(icao):
    conn = sqlite3.connect("flight_game.db")
    cur = conn.cursor()

    cur.execute("SELECT ident, name, municipality FROM airport WHERE ident = ?", (icao,))
    row = cur.fetchone()

    conn.close()

    if row:
        return jsonify({
            "ICAO": row[0],
            "Name": row[1],
            "Municipality": row[2]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(port=3000, debug=True)