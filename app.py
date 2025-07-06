from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/health')
def health_check():
    """Health check endpoint to verify server status"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'service': 'SmileItsSunnah Voice Agent',
        'version': '1.0.0'
    }), 200

@app.route('/')
def home():
    """Root endpoint"""
    return jsonify({
        'message': 'Welcome to SmileItsSunnah Voice Agent',
        'endpoints': {
            'health': '/health',
            'home': '/'
        }
    }), 200

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Get host from environment variable or default to localhost
    host = os.environ.get('HOST', '127.0.0.1')
    
    print(f"Starting server on {host}:{port}")
    print(f"Health check available at: http://{host}:{port}/health")
    
    app.run(host=host, port=port, debug=True)
