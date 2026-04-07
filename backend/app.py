import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from database import init_db, get_db
from scoring import calculate_yield

load_dotenv()

app = Flask(__name__)

# Restrict CORS to your GitHub Pages frontend
CORS(app, origins=[
    "https://foreverforward760-crypto.github.io",
    "http://localhost:3000",   # local dev
    "http://127.0.0.1:5500",   # VS Code Live Server
])

app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-me')

# Initialize database on startup
init_db()


@app.route('/api/health', methods=['GET'])
def health():
    """Health check — confirm backend is live."""
    return jsonify({"status": "ok", "version": "SAP v3.0"})


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """
    Receive carrier metrics, return yield score + stage, store result.

    Expected JSON body:
    {
        "hos": 6,
        "volatility": 4,
        "comm_quality": 7,
        "recovery_days": 3,
        "carrier_name": "Meridian Freight LLC",  // optional
        "mc_number": "MC-1042398"                // optional
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    hos           = data.get('hos')
    volatility    = data.get('volatility')
    comm_quality  = data.get('comm_quality')
    recovery_days = data.get('recovery_days')
    carrier_name  = data.get('carrier_name', 'Unknown')
    mc_number     = data.get('mc_number', '')

    # Validate required fields
    required = [('hos', hos), ('volatility', volatility),
                ('comm_quality', comm_quality), ('recovery_days', recovery_days)]
    for field, val in required:
        if val is None:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Run SAP scoring (server-side, logic hidden from browser)
    result = calculate_yield(
        int(hos), int(volatility), int(comm_quality), int(recovery_days)
    )

    # Store in database
    with get_db() as conn:
        conn.execute('''
            INSERT INTO calculations
            (timestamp, hos, volatility, comm_quality, recovery_days,
             yield_score, stage, carrier_name, mc_number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            datetime.utcnow().isoformat(),
            hos, volatility, comm_quality, recovery_days,
            result['score'], result['stage'],
            carrier_name, mc_number
        ))

    return jsonify({
        "yield_score": result['score'],
        "stage":       result['stage'],
        "tension":     result['tension'],
        "label":       result['label'],
        "guidance":    result['guidance'],
        "message":     "Calculation stored"
    })


@app.route('/api/recent', methods=['GET'])
def api_recent():
    """Return last N calculations for the dashboard (default 20)."""
    limit = request.args.get('limit', 20, type=int)
    with get_db() as conn:
        rows = conn.execute('''
            SELECT timestamp, hos, volatility, comm_quality, recovery_days,
                   yield_score, stage, carrier_name, mc_number
            FROM calculations
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,)).fetchall()
    return jsonify([dict(row) for row in rows])


@app.route('/api/stats', methods=['GET'])
def api_stats():
    """Summary stats for the dashboard metrics panel."""
    with get_db() as conn:
        total = conn.execute('SELECT COUNT(*) FROM calculations').fetchone()[0]
        avg_score = conn.execute(
            'SELECT AVG(yield_score) FROM calculations'
        ).fetchone()[0]
        stage8_count = conn.execute(
            'SELECT COUNT(*) FROM calculations WHERE stage = 8'
        ).fetchone()[0]
    return jsonify({
        "total_calculations": total,
        "avg_yield_score":    round(avg_score, 1) if avg_score else 0,
        "stage8_trap_count":  stage8_count
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
