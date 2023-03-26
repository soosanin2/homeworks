import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

@app.route('/hello')
def hello_world():
    logging.debug("log DEBUG Message")
    logging.info("log INFO")
    logging.warning("log WARNING")
    logging.error("log ERROR")
    logging.critical("A message of CRITICAL severity")
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

