from flask import Flask, render_template, request, redirect, url_for, session
from utils.document_preprocess import process_document
from utils.embedding import create_embeddings
from utils.vector_db import VectorDB
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Vector DB
vector_db = VectorDB()

@app.route('/')
def index():
    # Clear session to start fresh if coming back to the upload page
    session.clear()
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith(('pdf', 'doc', 'docx')):
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        session['filename'] = filename
        session['conversation'] = []  # Initialize conversation history
        return redirect(url_for('process_document_page'))
    return redirect(url_for('index'))

@app.route('/process_document')
def process_document_page():
    filename = session.get('filename')
    if filename:
        # Process the document to create embeddings
        text = process_document(filename)
        embeddings = create_embeddings(text)
        vector_db.store_embeddings(embeddings)
        return render_template('chat.html', filename=filename, conversation=[])
    return redirect(url_for('index'))

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form['question']
    if not question.strip():
        return "", 204  # Empty response for empty input
    
    answer = vector_db.query(question)
    # Store user question and answer for context
    vector_db.store_conversation(question, answer)

    # Maintain chat history in session
    conversation = session.get('conversation', [])
    conversation.append({"question": question, "answer": answer})
    session['conversation'] = conversation

    return render_template('chat.html', filename=session.get('filename'), conversation=conversation)

@app.route('/refresh_chat', methods=['POST'])
def refresh_chat():
    # Clear conversation history but keep the document
    session['conversation'] = []
    return render_template('chat.html', filename=session.get('filename'), conversation=[])

@app.route('/upload_new_document', methods=['POST'])
def upload_new_document():
    # Clear all session data and redirect to upload page
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
