from sentence_transformers import SentenceTransformer

# Initialize the SentenceTransformer model (for embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(chunks):
    """
    Create embeddings for a list of text chunks.
    Args:
        chunks (list of str): A list of text chunks to embed.
    Returns:
        numpy.ndarray: Embeddings for the text chunks.
    """
    # Encode each chunk into embeddings
    embeddings = model.encode(chunks)
    return embeddings

def encode_question(question):
    """
    Encode the question into an embedding.
    Args:
        question (str): A single question string.
    Returns:
        numpy.ndarray: Embedding for the question.
    """
    return model.encode([question]).astype('float32')

