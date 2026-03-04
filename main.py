from flask import Flask, request
from loguru import logger

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_http():
    try:
        logger.info("Starting ETL")
        return "✅ ETL Pipeline Completed"
    except Exception as e:
        logger.error(str(e))
        return f"❌ ETL FAILED: {str(e)}", 500