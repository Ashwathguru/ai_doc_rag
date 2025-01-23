from sentence_transformers import SentenceTransformer

# Initialize the SentenceTransformer model (for embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(text):
    # Split text into chunks for embedding
    text_chunks = text.split('\n')
    embeddings = model.encode(text_chunks)
    return embeddings

def encode_question(question):
    # Encode the question into an embedding
    return model.encode([question]).astype('float32')
