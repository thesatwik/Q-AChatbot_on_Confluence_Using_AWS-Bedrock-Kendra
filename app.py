import streamlit as st
from kendra2bedrock import kendraSearch


st.title(f""":rainbow[Welcome, I am your assistant to help extract relavant information from TheSatwik Confluence Clould] :sunglasses: """)


# configuring values for session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# writing the message that is stored in session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# adding some special effects from the UI perspective
st.balloons()
st.snow()
# evaluating st.chat_input and determining if a question has been input
if question := st.chat_input("I am your helper to retrive relavant information from TheSatwik Confluence"):
    # with the user icon, write the question to the front end
    with st.chat_message("user"):
       # st.write("Hello 👋")
        st.markdown(question)
    ##with st.chat_message("assistant" "🤖"):
    ##    st.write("Hello 👋")
    # append the question and the role (user) as a message to the session state
    st.session_state.messages.append({"role": "user",
                                      "content": question})
    # respond as the assistant with the answer
    with st.chat_message("assistant"):
        # making sure there are no messages present when generating the answer
        message_placeholder = st.empty()
        # putting a spinning icon to show that the query is in progress
        with st.status("Determining the best possible answer from TheSatwik Library!", expanded=True) as status:
        ##with st.spinner("Determining the best possible answer from TheSatwik Library!") as status:
            # passing the question into the kendra search function, which later invokes the llm
            answer = kendraSearch(question)
            # writing the answer to the front end
            message_placeholder.markdown(f"{answer}",)
            # showing a completion message to the front end
            status.update(label="Question is Answered", state="complete", expanded=False)
    # appending the results to the session state
    st.session_state.messages.append({"role": "assistant",
                                      "content": answer})


