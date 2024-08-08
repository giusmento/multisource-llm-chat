from abc import ABC, abstractmethod

from src.decorators.Hello import hello_decorator
from src.globals import ALL_DOCUMENTS
from src.utils.random import random_string


#@hello_decorator
class AbstractSource(ABC):

    def __init__(self, splitter, embedder):
        self.id = random_string(20)
        self.splitter = splitter
        self.embedder = embedder
    @abstractmethod
    def schedule_on(self, cron):
        pass

    @abstractmethod
    def load_data(self):
        pass

    def run(self):
        documents = self.splitter.split_documents(self.load_data())
        ALL_DOCUMENTS.append(documents)
