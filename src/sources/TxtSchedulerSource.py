from src.sources.abc.ScheduledAbstractSource import ScheduledAbstractSource
from langchain_community.document_loaders import TextLoader

from src.splitter.Splitter import Splitter

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class TxtScheduledSource(ScheduledAbstractSource):

    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def get_schedule(self):
        super()
        return self.cron

    def schedule_on(self, cron):
        self.cron = cron

    def load_data(self):
        logger.info(f"id:{self.id} - Start Loading txt from {self.folder}")
        loader_txt = TextLoader(self.folder)
        return loader_txt.load()



