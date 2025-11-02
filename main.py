from app.api import api_application

if __name__ == "__main__":
    api_application.run(host="0.0.0.0", port=5000, debug=True)
