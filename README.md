# 🚀 Namma Support Crew: Tamil Nadu Consumer Helpdesk

Excited to share my latest GenAI project — **Namma Support Crew**, a multi-agent AI customer support application built using CrewAI, Python, Streamlit, and OpenAI.

The project is designed to support Tamil Nadu consumer queries by combining local RAG-based knowledge retrieval with live web search to provide relevant and up-to-date information.

## 🛠️ Technology Stack
* **Python** – Core programming language
* **CrewAI** – Multi-agent orchestration and sequential workflow
* **Streamlit** – Interactive UI with custom HTML/CSS and branding
* **OpenAI** – LLM-powered agent reasoning

## 🔧 Tools Implemented
* **TXTSearchTool** – Retrieves information from the local `tn_consumer_guide.txt` knowledge base.
* **SerperDevTool** – Performs live web searches when additional or updated information is required.
* **Custom `@tool`** – Formats and enriches incoming consumer queries before processing.

## 🤖 Multi-Agent Workflow
The application follows a sequential CrewAI workflow with three specialized agents:

1. **Direct Support Specialist**  
   Analyzes the consumer query and provides an initial response using the available public-service knowledge.
2. **Web & Document Search Specialist**  
   Searches both the local knowledge base and live web sources to retrieve relevant information and supporting references.
3. **Entry & Records Archivist**  
   Combines the agent outputs, structures the final response, and maintains a local record of queries and responses.

## 💡 Key Learning
Building this project gave me valuable hands-on experience in Multi-Agent AI, RAG, tool integration, web search, prompt orchestration, and GenAI application development.

## ⚙️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/CibiChakravarthyK4/TN-Consumer-helpdesk_Crew.git](https://github.com/CibiChakravarthyK4/TN-Consumer-helpdesk_Crew.git)
   cd TN-Consumer-helpdesk_Crew


## 📁 Project Structure
```text
TN-Consumer-helpdesk_Crew/
│
├── app.py                  # Main Streamlit application & CrewAI orchestration logic
├── tn_consumer_guide.txt   # Local RAG reference guide (Tamil Nadu utility data)
├── answers.txt             # Auto-generated runtime output logs & records
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (API keys - ignored by git)
└── README.md               # Project documentation

⚙️ Installation & Setup
Clone the Repository:


Install Dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your API keys:

Code snippet
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
Run the Streamlit App:

Bash
streamlit run app.py
