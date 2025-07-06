# SmileItsSunnah Voice Agent Server

A Python Flask server with health check endpoint for the SmileItsSunnah Voice Agent project.

## Features

- Flask web server
- Health check endpoint at `/health`
- Production-ready with Gunicorn
- Configurable for different environments

## Setup

### Prerequisites
- Python 3.9+
- Virtual environment (automatically created)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

#### Development Mode
```bash
python app.py
```

Or use the startup script:
```bash
./start_server.sh
```

#### Production Mode
```bash
gunicorn -c gunicorn.conf.py app:app
```

## Endpoints

### Health Check
- **URL**: `/health`
- **Method**: GET
- **Response**: 
```json
{
  "status": "healthy",
  "timestamp": "2025-07-06T23:28:12.123456",
  "service": "SmileItsSunnah Voice Agent",
  "version": "1.0.0"
}
```

### Home
- **URL**: `/`
- **Method**: GET
- **Response**: Welcome message and available endpoints

## Configuration

The server can be configured using environment variables:

- `PORT`: Server port (default: 5000)
- `HOST`: Server host (default: 127.0.0.1)
- `FLASK_ENV`: Environment mode (development/production)

## Project Structure

```
.
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── gunicorn.conf.py    # Gunicorn production config
├── requirements.txt    # Python dependencies
├── start_server.sh     # Startup script
└── README.md          # This file
```

## Testing the Health Endpoint

Once the server is running, you can test the health endpoint:

```bash
curl http://localhost:5000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-07-06T23:28:12.123456",
  "service": "SmileItsSunnah Voice Agent",
  "version": "1.0.0"
}
```
