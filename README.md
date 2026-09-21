Markdown
# 🏛️ Namma Support Crew: Tamil Nadu Consumer Helpdesk

> A Multi-Agent AI Customer Support System built for Tamil Nadu public utilities and citizen services, powered by CrewAI, local Text RAG, live web search, and a high-end Streamlit UI.

## 🚀 Overview
**Namma Support Crew** bridges the gap between citizens and public utility information. Juggling multiple platforms for services like TNEB (Electricity), transport, and consumer grievances can be tedious. This system deploys an automated multi-agent workflow that acts as a specialized digital helpdesk, fetching verifiable answers from local documentation and the live web while ensuring security and compliance logging.

## 🛠️ Architecture & Multi-Agent Workflow
The application uses a **Sequential Process** via CrewAI, coordinating three distinct specialized agents:

1. **Direct Support Specialist (Agent 1):** Analyzes the incoming query and delivers primary advisory support using domain knowledge.
2. **Web & Document Search Specialist (Agent 2):** Queries local text reference files (`tn_consumer_guide.txt`) and live web sources using custom tools to retrieve up-to-date guidelines.
3. **Entry & Records Archivist (Agent 3):** Compiles the final response structure and automatically logs all interaction data locally into `answers.txt`.

## 🧰 Tech Stack & Tools
* **Core Language:** Python
* **Orchestration:** [CrewAI](https://www.crewai.com/)
* **Interface:** [Streamlit](https://streamlit.io/) (featuring custom Google Fonts 'Poppins', custom styling, and Tamil Nadu emblem branding)
* **LLM Provider:** OpenAI
* **Search Tools:** `SerperDevTool` (Live Web Search), `TXTSearchTool` (Local RAG)
* **Custom Code Utilities:** Custom `@tool` decorator for query formatting and metadata tagging.


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

Bash
git clone [https://github.com/CibiChakravarthyK4/TN-Consumer-helpdesk_Crew.git](https://github.com/CibiChakravarthyK4/TN-Consumer-helpdesk_Crew.git)
cd TN-Consumer-helpdesk_Crew
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
