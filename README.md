# 📖 AI Story Generator

An interactive **AI Story Generator** built with **Streamlit**, **LangChain**, and **Ollama**.

The application allows users to generate creative stories by customizing the language, tone, category, length, characters, time period, creativity level, grammar level, and target audience.

## ✨ Features

* 🤖 AI-powered story generation
* 🌐 Multiple language support:

  * English
  * Telugu
  * Hindi
  * Tamil
  * Urdu
  * Kannada
  * Chinese
* 🎭 Different story tones:

  * Friendly
  * Narrative
  * Poetic
* 📚 Multiple story categories:

  * Thriller
  * Horror
  * Suspense
  * Adventure
  * Comedy
  * Family
  * Drama
  * Fantasy
* 📝 Custom story ideas
* 👤 Custom character names
* 📄 Adjustable story length from 1–10 paragraphs
* 🎨 Creativity levels:

  * Low
  * Medium
  * High
* 🕰️ Different time periods:

  * Ancient
  * Modern
  * Future
* 🎯 Target audience selection
* ✍️ Grammar level selection
* 🔄 Originality control
* ⚡ Interactive Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Web application framework
* **LangChain** – LLM application framework
* **Ollama** – Local AI model runtime
* **Llama 3.1** – Language model

## 📁 Project Structure

```text
Story_Generator/
│
├── story.py
└── README.md
```

## ⚙️ Requirements

Make sure you have the following installed:

* Python 3.9 or later
* Streamlit
* LangChain
* LangChain Core
* Ollama
* Llama 3.1 model

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Vijayalakshmi-42/Story_Generator.git
```

### 2. Navigate to the project directory

```bash
cd Story_Generator
```

### 3. Install the required Python packages

```bash
pip install streamlit langchain langchain-core langchain-ollama
```

### 4. Install Ollama

Download and install Ollama from the official website:

https://ollama.com/

### 5. Download the Llama 3.1 model

After installing Ollama, run:

```bash
ollama pull llama3.1
```

Make sure Ollama is running before starting the application.

## ▶️ Run the Application

Run the following command from the project directory:

```bash
streamlit run story.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

## 🖥️ How to Use

1. Start the Streamlit application.
2. Select your preferred **language**.
3. Choose the desired **tone**.
4. Enter your **story idea**.
5. Select the number of paragraphs.
6. Choose the grammar level.
7. Select the story category.
8. Enter character names.
9. Select the time period.
10. Choose the creativity level.
11. Select the target audience.
12. Click **Generate Story**.
13. The AI-generated story will appear on the page.

## 🧠 How It Works

The application uses **LangChain** to create a structured prompt based on the user's selections.

The generated prompt contains information such as:

```text
Language
Tone
Target Audience
Creativity
Time Period
Grammar Level
Story Length
Category
Story Idea
Character Names
```

This prompt is sent to the locally running **Llama 3.1 model through Ollama**, which generates the story.

## 🔒 Privacy

The application uses Ollama to run the language model locally. No API key is required for the Llama 3.1 model when using the local Ollama setup.

## 📌 Future Improvements

Possible future improvements include:

* Download generated stories as PDF or TXT
* Story history
* User authentication
* Additional AI models
* More language options
* Image generation for stories
* Voice narration
* Improved UI and themes
* Cloud deployment


