from abc import abstractmethod

from src.embedding.Embedding import Embedding
from src.sources.abc.AbstractSource import AbstractSource
from src.splitter.Splitter import Splitter


class ScheduledAbstractSource(AbstractSource):

    def __init__(self):
        splitter = Splitter()
        embedder = Embedding()
        super().__init__(splitter,embedder)

    @abstractmethod
    def schedule_on(self, cron):
        pass

    @abstractmethod
    def get_schedule(self):
        pass

