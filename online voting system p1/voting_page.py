import streamlit as st
import mysql.connector as m

mydb = m.connect(
    host="localhost",
    user="root",
    password="***********",
    database="vote"
)
mycursor = mydb.cursor()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False  
if "voted" not in st.session_state:
    st.session_state.voted = False 
if "selected_candidate" not in st.session_state:
    st.session_state.selected_candidate = None  

def authenticate_voter(input_1, input_2):
    mycursor.execute("SELECT adhar_NO, vid, has_voted FROM voter WHERE adhar_NO = %s AND vid = %s", (input_1, input_2))
    voter = mycursor.fetchone()

    if voter:
        adhar_no, vid, has_voted = voter
        st.session_state.vid = vid 
        if has_voted == 0:
            st.success("Authentication successful! You can now vote.")
            st.session_state.authenticated = True  
        else:
            st.error("You have already cast your vote.")
    else:
        st.error("Invalid Aadhaar number or password.")

st.markdown("<h1 style='text-align: center;'>Welcome to Online Voting System</h1>", unsafe_allow_html=True)

input_1 = st.text_input('Enter your Aadhaar Number:')
input_2 = st.text_input('Enter your Password:', type="password")  

if st.button('Submit'):
    if len(input_1) == 8 or len(input_2) == 10: 
        authenticate_voter(input_1, input_2)
    else:
        st.error("Please enter valid Aadhaar (8 digits) and Password (10 characters).")

if st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center;'>CAST YOUR VOTE</h1>", unsafe_allow_html=True)

    mycursor.execute("SELECT sl_no, name FROM candidates")
    candidates = mycursor.fetchall()  
    
    if st.session_state.voted:
        st.warning("You have already cast your vote. Please rerun the program to vote again.")
    else:
        selected_candidate = st.radio(
            "Select a candidate to vote for:",
            options=[name for _, name in candidates],
            index=None  
        )

        if selected_candidate:
            st.session_state.selected_candidate = selected_candidate

        if st.button("Submit Vote") and st.session_state.selected_candidate:
            selected_sl_no = next(sl_no for sl_no, name in candidates if name == st.session_state.selected_candidate)

            mycursor.execute("UPDATE votes SET total_votes = total_votes + 1 WHERE sl_no = %s", (selected_sl_no,))
            
            mycursor.execute("UPDATE voter SET has_voted = 1 WHERE vid = %s", (st.session_state.vid,))
            mydb.commit()

            st.session_state.voted = True

            st.success(f"You have successfully cast your vote for {st.session_state.selected_candidate}.")
