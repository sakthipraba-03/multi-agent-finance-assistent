# AI-Powered Market Voice Assistant
This is a voice-enabled multi-agent assistant designed for portfolio managers to get real-time briefings on **Asia tech stock exposure** and **earnings surprises**. The system uses **Speech-to-Text (STT)** to process spoken queries, retrieves answers using a **Retrieval-Augmented Generation (RAG)** pipeline, and responds through a simple web interface.

## Use Case
> Every trading day at 8 AM, a portfolio manager asks:
        “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”
> The system replies with:
        “Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday. TSMC beat estimates by 4%, Samsung missed by 2%…”

## System Architecture
![System Architecture](./assets/architecture.png)

## Components Used

| Component        | Tools / Framework            |
|------------------|------------------------------|
| Voice-to-Text (STT) | `Whisper`                 |
| STT Recording    | `sounddevice`                |
| Embeddings       | `sentence-transformers`      |
| Vector Store     | `FAISS`                      |
| LLM              | `DeepSeek-r1`                |
| Interface        | `Streamlit`                  |
| PDF Parsing      | `pdfplumber`                 |


## Agent Roles

| Agent            | Role / Responsibility                                              |
|------------------|--------------------------------------------------------------------|
|Voice Agent       | Converts user voice input to text using Whisper                    |
|Retriever Agent   | Retrieves relevant chunks from financial documents via FAISS       |
|Language Agent    | Synthesizes context into final answer using an LLM                 |
|Fallback Logic    | Checks retrieval confidence and prompts user to rephrase if too low|
|Interface Agent   | Displays results and manages user interaction via Streamlit        |

## Setup Instructions

### 1. Clone the repo
git clone https://github.com/sakthipraba-03/multi-agent-finance-assistant.git
cd multi-agent-finance-assistant

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
Run: streamlit run streamlit_app.py

## Framework & Toolkit Comparison
| Task                | Toolkit Chosen         | Alternatives Considered      | Why This Was Chosen                          |
|---------------------|------------------------|------------------------------|----------------------------------------------|
| Speech-to-Text (STT)| `Whisper`              | Vosk, AssemblyAI, Google STT | Accurate, open-source, multilingual          |
| UI / Frontend       | `Streamlit`            | Flask, Gradio                | Easiest integration for voice input + output |
| Vector DB           | `FAISS`                | Pinecone, Chroma             | Fast, lightweight, local                     |
| Embeddings          | `sentence-transformers`| OpenAI, Cohere               | Free, local, effective on PDF chunks         |
| LLM                 | `DeepSeek-r1`          | GPT-3.5, Claude              | Flexible, supports local + cloud inference   |