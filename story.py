import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

st.set_page_config(page_title="AI Story Generator", layout="wide")

st.title("📖 AI Story Generator")

# -----------------------------
# Initialize Model
# -----------------------------
if "model" not in st.session_state:
    st.session_state["model"] = init_chat_model(
        model="llama3.1:latest",
        model_provider="ollama",
    )
# -----------------------------
# Prompt Template
# -----------------------------
if "template" not in st.session_state:
    st.session_state["template"] = PromptTemplate(
        input_variables=[
            "language",
            "tone",
            "storyIdea",
            "length",
            "grammar",
            "plagiarism",
            "categories",
            "character_names",
            "time_period",
            "creativity",
            "audience",
        ],
        template="""
You are a professional story writer.

Write a story in {language}. Every word in the output must be in {language}, even if the user's input is in English.

Requirements:
- Tone: {tone}
- Target Audience: {audience}
- Creativity Level: {creativity}
- Time Period: {time_period}
- Grammar Level: {grammar}
- Plagiarism Level: {plagiarism}
- Story Length: {length} paragraphs
- Category: {categories}
- Story Idea: {storyIdea}
- Character Names: {character_names}

Avoid emojis.
Generate an engaging and original story.
"""
    )

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Story Settings")

language = st.sidebar.selectbox(
    "Language",
    ["English", "Telugu", "Hindi", "Tamil", "Urdu", "Kannada", "Chinese"]
)

tone = st.sidebar.selectbox(
    "Tone",
    ["Friendly", "Narrative", "Poetic"]
)

storyIdea = st.sidebar.text_area(
    "Story Idea",
    placeholder="Describe your story..."
)

length = st.sidebar.slider(
    "Number of Paragraphs",
    1,
    10,
    3
)

grammar = st.sidebar.selectbox(
    "Grammar Level",
    ["Beginner", "Intermediate", "Professional"]
)

plagiarism = st.sidebar.slider(
    "Originality (%)",
    0,
    100,
    100
)

categories = st.sidebar.radio(
    "Category",
    [
        "Thriller",
        "Horror",
        "Suspense",
        "Adventure",
        "Comedy",
        "Family",
        "Drama",
        "Fantasy",
    ]
)

characterNames = st.sidebar.text_area(
    "Character Names",
    placeholder="Alice, Bob, Charlie"
)

timePeriod = st.sidebar.selectbox(
    "Time Period",
    ["Ancient", "Modern", "Future"]
)

creativity = st.sidebar.selectbox(
    "Creativity",
    ["Low", "Medium", "High"]
)

audience = st.sidebar.selectbox(
    "Target Audience",
    ["Toddlers", "Kids", "Adults", "Old People"]
)

submit_button = st.sidebar.button(
    "Generate Story",
    use_container_width=True,
    type="primary"
)

# -----------------------------
# Generate Story
# -----------------------------
if submit_button:

    final_prompt = st.session_state["template"].format(
        language=language,
        tone=tone,
        storyIdea=storyIdea,
        length=length,
        grammar=grammar,
        plagiarism=plagiarism,
        categories=categories,
        character_names=characterNames,
        time_period=timePeriod,
        creativity=creativity,
        audience=audience,
    )

    with st.spinner("Generating your story..."):
        response = st.session_state["model"].invoke(final_prompt)

    st.subheader("Generated Story")
    st.write(response.content)