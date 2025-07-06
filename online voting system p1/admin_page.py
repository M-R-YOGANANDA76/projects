
import streamlit as st
import mysql.connector

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "clicked" not in st.session_state:
    st.session_state.clicked = False
if "input1" not in st.session_state:
    st.session_state.input1 = ""
if "input2" not in st.session_state:
    st.session_state.input2 = ""
if "input3" not in st.session_state:
    st.session_state.input3 = ""
if "input4" not in st.session_state:
    st.session_state.input4 = ""
if "input5" not in st.session_state:
    st.session_state.input5 = ""
if "input6" not in st.session_state:
    st.session_state.input6 = ""
if "input7" not in st.session_state:
    st.session_state.input7 = ""


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="vote"
)
mycursor = mydb.cursor()

admin_menu = {
    1: "Register candidate",
    2: "Register voter",
    3: "View results",
    4: "view not voted members ",
    5: "Exit"
}

# Function to register voter
def register_voter(vid, name, address, gender, adhar_number):
    try:
        query = "INSERT INTO voter (vid, name, address, gender, adhar_no) VALUES (%s, %s, %s, %s, %s);"
        values = (vid, name, address, gender, adhar_number)
        mycursor.execute(query, values)
        mydb.commit()
        st.success("Voter registered successfully!")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")

# Function to register candidate
def register_candidate(sl_no, name):
    try:
        query = "INSERT INTO candidates (sl_no, name) VALUES (%s, %s);"
        values = (sl_no, name)
        query2 = "INSERT INTO votes (sl_no, total_votes) VALUES (%s, %s);"
        value = (sl_no, 0)
        mycursor.execute(query, values)
        mycursor.execute(query2, value)
        mydb.commit()
        st.success("Candidate registered successfully!")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")

# Fetch admin credentials from the database
mycursor.execute("SELECT user_name, password FROM admin")
details = mycursor.fetchall()
admin_credentials = {user: pwd for user, pwd in details}  # Store in a dictionary

# Login fields
st.session_state.input6 = st.text_input("Enter admin user_name:", value=st.session_state.input6, key="user_name")
st.session_state.input7 = st.text_input("Enter admin password:", type="password", value=st.session_state.input7, key="password")

# Login button logic
if st.button("Log in", key="admin"):
    if st.session_state.input6 in admin_credentials and st.session_state.input7 == admin_credentials[st.session_state.input6]:
        st.session_state.logged_in = True  
        st.success("Login successful!")
    else:
        st.session_state.logged_in = False
        st.error("Admin is not registered or incorrect credentials.")

# **Only show options if the user is logged in**
if st.session_state.logged_in:
    st.table([{"sl_no": key, "menu": value} for key, value in admin_menu.items()])
    opt = st.number_input("Enter the correct option:", min_value=1, max_value=4, step=1)

    if st.button("Submit", key="sub1"):
        st.session_state.clicked = True

    if st.session_state.clicked:
        if opt == 1:
            st.write("Register candidate")
            st.session_state.input1 = st.text_input("Enter candidate ID:", value=st.session_state.input1, key="cand_id")
            st.session_state.input2 = st.text_input("Enter candidate name:", value=st.session_state.input2, key="cand_name")
            if st.button("Register Candidate", key="register_cand"):
                register_candidate(st.session_state.input1, st.session_state.input2)

        elif opt == 2:
            st.write("Register voter")
            st.session_state.input1 = st.text_input("Enter your voter ID:", value=str(st.session_state.input1), key="voter_id")
            st.session_state.input2 = st.text_input("Enter your name:", value=st.session_state.input2, key="voter_name")
            st.session_state.input3 = st.text_input("Enter your address:", value=st.session_state.input3, key="voter_address")
            st.session_state.input4 = st.text_input("Enter your gender:", value=st.session_state.input4, key="voter_gender")
            st.session_state.input5 = st.text_input("Enter your adhar number:", value=st.session_state.input5, key="voter_adhar")
            if st.button("Register voter", key="register_voter"):
                register_voter(st.session_state.input1, st.session_state.input2, st.session_state.input3, st.session_state.input4, st.session_state.input5)

        elif opt == 3:
            st.write("View results")
            mycursor.execute("SELECT sl_no, name FROM candidates WHERE sl_no IN (SELECT sl_no FROM votes WHERE total_votes=(SELECT MAX(total_votes) FROM votes));")
            for result in mycursor:
                st.header(f"The winner is: {result[1]} with ID {result[0]}")
        elif opt==4:
            st.markdown("<h1 style='text-align: center;'>non participated members</h1>", unsafe_allow_html=True)
            mycursor.execute("select count(*) from voter")
            candidates = mycursor.fetchall()  
            for number in candidates:
                for num in number:
                    count=num
            mycursor.execute("select count(*) from voter where has_voted=0;")
            candidate = mycursor.fetchall()  
            for number1 in candidate:
                for  num2 in number1:
                    count2=num2
            
            mycursor.execute("SELECT name FROM voter where has_voted=0;") 
            for k in mycursor:
                for l in k:
                    st.write(l)
            
            st.write(f"out of {count} / {count2} has not voted")
        elif opt == 5:
            st.write("Exit")
            st.stop()

        else:
            st.error("Invalid option! Please choose a valid menu item.")
else:
    st.warning("Please log in first.")
