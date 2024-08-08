class FAISSDatabase(object):

    def __init__(self):
        pass

    def refresh(self):
        FAISS.from_documents(all_documents, embeddings)