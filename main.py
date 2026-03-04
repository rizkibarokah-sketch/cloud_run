
from loguru import logger


def hello_http(request):
    try:
        logger.info("Starting ETL")


        return "✅ ETL Pipeline Completed"

    except Exception as e:
        logger.error(str(e))
        return f"❌ ETL FAILED: {str(e)}", 500