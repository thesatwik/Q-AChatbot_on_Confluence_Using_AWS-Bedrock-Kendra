import streamlit as st
import io ##For Audio
from gtts import gTTS ##For audio
from io import BytesIO
from kendra2bedrock import kendraSearch

##st.set_page_config(page_title="SatwikChatbot", page_icon="🤖", layout="centered", initial_sidebar_state="auto", menu_items="About")


##Set page Config ####
st.set_page_config(
    page_title="TheSatwik-Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.thesatwik.com',
        'Report a bug': "https://www.thesatwik.com",
        'About': "# TheSatwikChatbot V2 - This helps Extracts Info from TheSatwik Confluence"
    }
)

'''
# :blue[TheSatwik Chatbot] 🤖
helps you extract relavant information from _**TheSatwik Confluence Cloud**_
'''

##Set Page Title
st.title(f""":rainbow[Welcome, I am your assistant to help extract relavant information from TheSatwik Confluence Clould] :sunglasses: """)


# configuring values for session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# writing the message that is stored in session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# adding some special effects from the UI perspective
##st.balloons()
st.snow()

#####Setting some Image for the site. Store the image in the same location where this script is placed. 
##st.image('chatbot.png', caption='How can I help you today?', use_column_width='auto')
##st.image('hi-robot.gif', caption='How can I help you today?', use_column_width='auto')
st.image('robo1.png', caption='How can I help you today?', use_column_width='auto')

#####

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
                      
                ###Trying out audio from here
            sound_file = BytesIO()
            tts = gTTS(f"{answer}", lang='en')
            tts.write_to_fp(sound_file)
            audio_output= st.audio(sound_file)
             # writing the answer to the front end
            message_placeholder.markdown(f"{answer}")

            # showing a completion message to the front end
            status.update(label="Question is Answered!! You can listen to this reponse by playing beloww audio", state="complete", expanded=True)
    # appending the results to the session state
    st.session_state.messages.append({"role": "assistant",
                                      "content": answer})
    # st.session_state.messages.append({"role": "assistant",
    #                                   "content": audio_output})


