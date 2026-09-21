import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.tools import tool
from crewai_tools import SerperDevTool, TXTSearchTool

# Load environment variables from .env
load_dotenv()

# Streamlit Page Setup
st.set_page_config(
    page_title="Namma Support Crew: Tamil Nadu Consumer Helpdesk",
    page_icon="🏛️",
    layout="centered",
)

# --- CUSTOM CSS FOR TOP-NOTCH UI ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    /* Global Light Theme & Font Override */
    .stApp {
        background-color: #ffffff;
        color: #1e293b;
        font-family: 'Poppins', sans-serif;
        background-image: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)), 
                          url('https://upload.wikimedia.org/wikipedia/commons/b/b3/Emblem_of_Tamil_Nadu.svg');
        background-repeat: no-repeat;
        background-position: center 60vh;
        background-size: 350px 350px;
    }

    /* Custom Heading Layout & Styling */
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 2.3rem;
        color: #0f172a;
        margin-bottom: 0px;
        line-height: 1.2;
    }
    
    .sub-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.5rem;
        color: #0284c7;
        margin-top: 5px;
        margin-bottom: 15px;
        line-height: 1.2;
    }

    .description-text {
        font-family: 'Poppins', sans-serif;
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 25px;
    }

    /* Input Box Customization */
    .stTextInput label {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #1e293b !important;
    }

    /* Button Styling */
    .stButton button {
        background-color: #0284c7;
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #0369a1;
        box-shadow: 0 6px 8px -1px rgba(0, 0, 0, 0.15);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- TWO-LINE CUSTOM HEADER STRUCTURE ---
st.markdown(
    '<div class="main-title">🏛️ Namma Support Crew</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">Tamil Nadu Consumer Helpdesk</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="description-text">Multi-Agent Customer Support System featuring'
    " <b>Text Document RAG</b>, <b>Web Search</b>, <b>Custom Tools (@tool)</b>,"
    " and <b>Guardrails</b>.</div>",
    unsafe_allow_html=True,
)

# User Input Box
user_query = st.text_input(
    "Enter your support query (e.g., How do I register a consumer grievance or check TNEB bill status?):"
)


# --- 1. GUARDRAILS IMPLEMENTATION ---
def input_guardrail(query: str) -> tuple[bool, str]:
  """Validates user input query for safety and relevance."""
  if not query or len(query.strip()) < 3:
    return False, "Query is too short. Please provide a descriptive question."

  forbidden_words = ["hack", "exploit", "malware", "bypass"]
  if any(word in query.lower() for word in forbidden_words):
    return (
        False,
        "Guardrail Triggered: Query contains restricted or prohibited terms.",
    )

  return True, "Passed"


# --- 2. CUSTOM TOOL DECORATOR IMPLEMENTATION ---
@tool("Consumer Query Formatter")
def format_consumer_query_tool(query_text: str) -> str:
  """Formats and tags incoming consumer queries with standard Tamil Nadu helpdesk metadata."""
  cleaned = query_text.strip().capitalize()
  formatted_output = (
      f"[TN-HELPDESK-LOG] Region: Tamil Nadu | Processed Query: {cleaned} | Status:"
      " Verified"
  )
  return formatted_output


if st.button("Run Support Crew"):
  # Apply Input Guardrail Check
  is_safe, message = input_guardrail(user_query)

  if not is_safe:
    st.error(f"🛡️ Security Guardrail Blocked Request: {message}")
  else:
    with st.spinner(
        "Running Namma Support Crew with Text RAG, Web Search & Tools..."
    ):
      try:
        # Initialize Tools
        search_tool = SerperDevTool()
        txt_tool = TXTSearchTool(txt="tn_consumer_guide.txt")
        custom_formatter = format_consumer_query_tool

        # Agent 1: Assistant
        assistant_agent = Agent(
            role="Direct Support Specialist",
            goal=(
                "Answer the user's consumer support query directly using core"
                " knowledge about Tamil Nadu services."
            ),
            backstory=(
                "You are an experienced customer support professional specializing"
                " in Tamil Nadu public utilities, consumer protection, and"
                " citizen services."
            ),
            verbose=True,
            memory=False,
        )

        # Agent 2: Web & Document Search Assistant
        web_search_agent = Agent(
            role="Web and Document Search Specialist",
            goal=(
                "Search both local text reference guides and the web to retrieve"
                " accurate procedures or guidelines."
            ),
            backstory=(
                "You are an intelligent data retrieval agent capable of"
                " querying local text documents, gathering live links, and"
                " formatting queries using specialized tools."
            ),
            tools=[txt_tool, search_tool, custom_formatter],
            verbose=True,
            memory=False,
        )

        # Agent 3: Entry Agent
        entry_agent = Agent(
            role="Entry and Records Archivist",
            goal=(
                "Compile responses, write them cleanly into answers.txt, and"
                " structure the final output."
            ),
            backstory=(
                "You manage compliance logs and save all customer queries and"
                " structured answers locally."
            ),
            verbose=True,
            memory=False,
        )

        # Sequential Tasks
        task_direct = Task(
            description=(
                f"Provide a direct advisory answer for: {user_query}"
            ),
            expected_output="A clear direct response addressing the user issue.",
            agent=assistant_agent,
        )

        task_web_and_rag = Task(
            description=(
                f"Search the local text documentation and the web for"
                f" up-to-date sources regarding: {user_query}. Use the custom"
                " query formatter tool to tag the process."
            ),
            expected_output=(
                "A detailed web and document-sourced response with official"
                " references."
            ),
            agent=web_search_agent,
        )

        task_save = Task(
            description=(
                "Take outputs from previous tasks, compile them cleanly,"
                " and save everything into 'answers.txt'."
            ),
            expected_output=(
                "Confirmation that records are saved and answers are compiled."
            ),
            agent=entry_agent,
            output_file="answers.txt",
        )

        # Sequential Crew Workflow
        support_crew = Crew(
            agents=[assistant_agent, web_search_agent, entry_agent],
            tasks=[task_direct, task_web_and_rag, task_save],
            process=Process.sequential,
            verbose=True,
        )

        result = support_crew.kickoff()

        # Output Display
        st.success("Workflow executed successfully with all guardrails passed!")
        st.markdown("### 📋 Final Results Summary")
        st.markdown(str(result))

        if os.path.exists("answers.txt"):
          st.info(
              "💾 Successfully logged data and answers to local `answers.txt`."
          )

      except Exception as e:
        st.error(f"An error occurred during execution: {e}")