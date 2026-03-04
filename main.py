import time
from loguru import logger

def main():
    logger.info("Starting loop...")

    for i in range(1, 101):
        logger.info(f"Hello World {i}")
        time.sleep(0.3)

    logger.info("Finished loop.")

if __name__ == "__main__":
    main()