import schedule
import logging
import time

from src.sources.TxtSchedulerSource import TxtScheduledSource

# Create a logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sources = [
    {"name": "load-one", "cron": 30, "type": "TxtSchedulerSource", "folder": "../data/txt-folder-one/wiki-sicily.txt"},
    {"name": "load-two", "cron": 60, "type": "TxtSchedulerSource", "folder": "../data/txt-folder-two/wiki-turin.txt"}
]

logger.info("Prepare globals")


logger.info("Start loading sources")
for source in sources:
    logger.info(f"Start source name:{source['name']} cron:{source['cron']}")
    run = TxtScheduledSource(source['folder']).run
    schedule.every(source['cron']).seconds.do(run)  # Run

logger.info("Start Vector DB")
vectorDB = FAISSDatabase()
schedule.every().seconds.do(vectorDB.refresh)  # Run


while True:
    schedule.run_pending()
    time.sleep(1)