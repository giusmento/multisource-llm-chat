from langchain_community.embeddings import HuggingFaceEmbeddings
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the path to the pre-trained model you want to use
modelPath = "sentence-transformers/all-MiniLM-l6-v2"

# Create a dictionary with model configuration options, specifying to use the CPU for computations
model_kwargs = {'device': 'cpu'}

# Create a dictionary with encoding options, specifically setting 'normalize_embeddings' to False
encode_kwargs = {'normalize_embeddings': False}


class Embedding(object):
    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(
            model_name=modelPath,  # Provide the pre-trained model's path
            model_kwargs=model_kwargs,  # Pass the model configuration options
            encode_kwargs=encode_kwargs  # Pass the encoding options
        )
        pass

    def get_embedder(self):
        return self.embedder
