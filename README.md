# Open Source RAG Application

This is an open-source **Retrieval Augmented Generation (RAG)** application built using the **Ollama Framework**, **FAISS vector store**, and the **Llama2 LLM**. The application allows users to upload a document (in PDF, DOC, or DOCX format) and then interact with it by asking questions through a chat interface. The system extracts embeddings from the document, stores them in a vector database (FAISS), and uses those embeddings to generate context-aware responses using the Llama2 language model.

## Features

- **Document Upload**: Users can upload a PDF, DOC, or DOCX file for processing.
- **Document Preprocessing**: Extracts text from the uploaded document and splits it into smaller chunks for efficient embedding storage.
- **Embedding Generation**: Uses **SentenceTransformer** to generate embeddings for each chunk of text from the document.
- **Vector Database (FAISS)**: Stores embeddings in a FAISS index for efficient similarity search.
- **Chat Interface**: Allows users to ask questions related to the document, with responses generated based on the most relevant context retrieved from the document using FAISS.
- **Context-Aware Responses**: The Llama2 model, accessed through the Ollama framework, uses document chunks retrieved from FAISS to generate accurate and relevant answers.

## Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.7 or higher
- **Flask**: Web framework for serving the app.
- **FAISS**: For vector search.
- **SentenceTransformers**: For generating sentence embeddings.
- **Ollama**: Interface for accessing the Llama2 model.
- **NumPy**: For numerical operations.

You can install the necessary Python packages by running:

```bash
pip install flask faiss-cpu sentence-transformers numpy ollama
```

## Folder Structure

```
/your_project
├── app.py                    # Main Flask application
├── utils/
│   ├── document_preprocess.py  # Document processing logic (extract text from PDFs, DOCX files)
│   ├── embedding.py           # Functions for creating embeddings
│   └── vector_db.py           # FAISS vector database implementation
├── uploads/                  # Folder to store uploaded files
├── templates/                 # HTML templates (index.html, chat.html)
└── static/                    # Static files (CSS, JS, etc.)
```

## How It Works

1. **Document Upload**: The user uploads a document via the web interface. The application supports **PDF**, **DOC**, and **DOCX** file formats.
   
2. **Text Extraction & Preprocessing**: Once a document is uploaded, it is processed using the `process_document()` function from `utils/document_preprocess.py`. The text is then split into smaller chunks using the `split_into_chunks()` function.

3. **Embedding Generation**: The text chunks are passed to the `create_embeddings()` function, which uses the **SentenceTransformer** model to generate embeddings for each chunk.

4. **Storing Embeddings**: The embeddings are stored in a **FAISS index** using the `store_embeddings()` method of the `VectorDB` class. This allows for efficient retrieval of relevant chunks of text during querying.

5. **Querying the Document**: When the user asks a question through the chat interface, the question is encoded into an embedding using the `encode_question()` function. The question embedding is then compared with the stored document embeddings in the FAISS index to find the most relevant document chunks.

6. **Generating Responses**: The most relevant chunks are passed to the **Llama2 model** via the **Ollama API**, which generates an answer based on the retrieved context.

7. **Maintaining Conversation History**: The user’s questions and the system's answers are stored in the session, allowing for a continuous conversation where the context can evolve over time.

## Endpoints

### `/`
- **GET**: The homepage where the user can upload a document.

### `/upload`
- **POST**: Handles file uploads. Supports PDF, DOC, and DOCX formats. Saves the uploaded file and starts the processing workflow.

### `/process_document`
- **GET**: Processes the uploaded document, extracts text, generates embeddings, and stores them in the FAISS vector database.

### `/chat`
- **POST**: Handles user queries. Queries the FAISS index for relevant context, generates a response using Llama2 via Ollama, and returns the answer along with the updated conversation.

### `/refresh_chat`
- **POST**: Clears the conversation history, but keeps the document.

### `/upload_new_document`
- **POST**: Clears all session data and redirects the user back to the upload page.

## Setup and Run

1. Clone the repository or download the project files to your local machine.

2. Install the required Python dependencies (listed above).

3. Run the Flask app:

```bash
python app.py
```

4. Open your browser and go to [http://localhost:5000](http://localhost:5000).

5. Upload a document and start interacting with it via the chat interface.

## Example Usage

1. **Upload Document**: Upload a PDF or DOCX document using the upload form on the homepage.

2. **Ask Questions**: After the document is processed, ask questions about the document. The application will retrieve relevant document chunks and generate answers based on the context.

3. **Maintain Conversation**: Ask multiple questions in sequence, and the app will keep track of the conversation history, maintaining context across different queries.

4. **Refresh or Upload New Document**: Refresh the chat history or upload a new document to start over.

