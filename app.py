import streamlit as st
from transformers import pipeline

# Lazy-load pipelines only when selected
@st.cache_resource
def get_pipeline(task_name):
    if task_name == "Question Answering":
        return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    elif task_name == "Summarization":
        return pipeline("summarization")
    elif task_name == "Translation":
        return pipeline("translation_en_to_fr")
    elif task_name == "Text Generation":
        return pipeline("text-generation", model="gpt2")
    return None

# Initialize history
if "history" not in st.session_state:
    st.session_state.history = []

# UI Layout
st.title("📚 AI-Powered Personal Study Assistant")
task = st.selectbox("Choose a Task", ["Question Answering", "Summarization", "Translation", "Text Generation"])

with st.form("user_input_form"):
    user_input = st.text_area("Enter your input", height=150)
    submit_button = st.form_submit_button("Submit")

# Process input
if submit_button and user_input:
    pipe = get_pipeline(task)

    if task == "Question Answering":
        # Using input as both question and context (you can improve this later)
        result = pipe(question=user_input, context=user_input)
        answer = result['answer']
    elif task == "Summarization":
        result = pipe(user_input, max_length=130, min_length=30, do_sample=False)
        answer = result[0]['summary_text']
    elif task == "Translation":
        result = pipe(user_input)
        answer = result[0]['translation_text']
    elif task == "Text Generation":
        result = pipe(user_input, max_length=50, num_return_sequences=1)
        answer = result[0]['generated_text']
    else:
        answer = "Please provide valid input."

    # Save to history
    st.session_state.history.append((task, user_input, answer))

    # Display result
    st.subheader("Result:")
    st.write(answer)

# Show conversation history
st.sidebar.title("📝 Conversation History")
for i, (task, query, response) in enumerate(st.session_state.history):
    with st.sidebar.expander(f"{i+1}. {task}"):
        st.markdown(f"**Input:** {query}")
        st.markdown(f"**Response:** {response}")
