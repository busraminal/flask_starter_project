from app import app
from waitress import serve

if __name__ == '__main__':
     #app.run(host='0.0.0.0', port=5011, debug=True, use_reloader=False)
     print("Starting the application with Waitress...")
     serve(app, host='0.0.0.0', port=5011)
