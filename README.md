# Python Socket Chat Application (Terminal Based)

A simple **terminal-based chat application** built using **Python sockets**.  
This project demonstrates basic **client-server communication** using TCP sockets and is ideal for beginners learning networking concepts in Python.

---

## 📌 Features

- Client–Server architecture
- Built using Python's built-in `socket` module
- Runs completely in the terminal
- Real-time message exchange
- Beginner-friendly and easy to understand

---

## 🗂️ Project Structure

chat_app/
│
├── server.py # Server-side code
└── client.py # Client-side code

yaml
Copy code

---

## 🛠️ Requirements

- Python 3.x installed on your system  
- Works on **Windows / Linux / macOS**
- No external libraries required

🚀 How to Run the Project (Step-by-Step)
1️⃣ Clone or Download the Project
You can either clone this repository or download the files manually.

bash
Copy code
git clone <your-repo-link>
OR
Create a folder named chat_app and place server.py and client.py inside it.

2️⃣ Start the Server
Open Terminal / Command Prompt, navigate to the project folder:

bash
Copy code
cd chat_app
python server.py
You should see:

pgsql
Copy code
Server is listening on port 5500...
⚠️ Keep this terminal open

3️⃣ Start the Client
Open a new terminal window, go to the same folder:

bash
Copy code
cd chat_app
python client.py
Now you can start typing messages from the client.

4️⃣ Chat Flow
Client sends a message

Server receives it

Server sends a response back

Communication happens via sockets

🧠 Concepts Used
TCP Sockets

Client-Server Model

socket.AF_INET

socket.SOCK_STREAM

Encoding & decoding messages

📚 Learning Purpose
This project is made for:

Python beginners

Students learning Computer Networks

Practice for GitHub portfolio

Understanding socket programming basics

🔮 Future Improvements (Optional)
Multiple client support (using threading)

Username-based chat

Client-to-client messaging

GUI using Tkinter

Message timestamps
