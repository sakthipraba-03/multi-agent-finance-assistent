# AI Tool Usage Log
This document summarizes the use of AI tools in this project, including:
- Prompts used to generate or assist code
- Steps in AI-assisted code generation
- Key model configurations and parameters


## 1. Prompts Used

### Whisper (STT)
> **Prompt:**  
> "How to transcribe audio from microphone using `openai/whisper-small` with Hugging Face and `sounddevice`?"

### RAG Pipeline
> **Prompt:**  
> "How to implement a RAG pipeline using FAISS and sentence-transformers for document retrieval and query answering with a local LLM like DeepSeek?"

### Streamlit Integration
> **Prompt:**  
> "Build a Streamlit app with a voice record button that runs Whisper STT and shows RAG-based output."

### Fallback Logic
> **Prompt:**  
> "Implement a fallback agent that checks LLM response confidence and prompts the user to rephrase if confidence is low."


## 2. Code Generation Steps

| Component / Feature        | Logic or Prompt Result                                                         |
|----------------------------|--------------------------------------------------------------------------------|
| STT Function (Whisper)     | Full function to record and transcribe mic input using Whisper + sounddevice   |
| FAISS vector store & Index | Embedded stock PDFs using sentence-transformers and indexed them in FAISS      |
| RAG Query Handling         | Retrieved top-k chunks from FAISS and passed them to LLM                       |
| LLM Integration            | Used local DeepSeek R1 model to generate responses from context                |               
| Prompt Template Design     | Constructed system prompt with retrieved context + user query for LLM          |
| Streamlit UI               | Created a voice-enabled Streamlit app with button, calling STT and RAG pipeline|
| Fallback Logic             | Checked confidence score and asked user to retry if score was too low          |


## 3. Model Parameters

| Model / Component        | Value / Configuration |
|--------------------------|-----------------------|
| **STT Model**            | `openai/whisper-small` (Hugging Face) |
| **Audio Sample Rate**    | `16,000 Hz` |
| **Embedding Model**      | `sentence-transformers/all-MiniLM-L6-v2` |
| **Vector Store**         | `FAISS`, top_k = 5 |
| **Confidence Threshold** | `0.65` for fallback |
| **LLM**                  | `DeepSeek r1` 7b model integrated locally using ollama|