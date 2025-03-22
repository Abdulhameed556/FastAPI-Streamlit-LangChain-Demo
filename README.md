# LangChain Essay & Poem Generator

This project is a simple **FastAPI**-based backend with a **Streamlit** frontend that generates essays and poems using two different Large Language Models (LLMs):

- **DeepSeek** (via OpenRouter) for **essay generation**
- **LLaMA-3** (via Groq API) for **poem generation**

## Features

- Uses **FastAPI** for the backend API.
- Implements **Streamlit** for a simple user interface.
- Utilizes **DeepSeek** (via OpenRouter) to generate structured essays.
- Uses **LLaMA-3 (Groq API)** to create child-friendly poems.
- Supports dynamic topic input for both essays and poems.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/https://github.com/Abdulhameed556/FastAPI-Streamlit-LangChain-Demo/langchain-essay-poem.git
   cd langchain-essay-poem
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your API keys:

   ```env
   OPENROUTER_API_KEY=your_openrouter_key
   GROQ_API_KEY=your_groq_key
   ```

## Running the Application

### Start FastAPI Backend

Run the FastAPI server with:

```bash
uvicorn fastapi_app:app --host localhost --port 8000
```

### Start Streamlit Frontend

Run the Streamlit app with:

```bash
streamlit run client.py
```

## API Endpoints

### Essay Generator (DeepSeek - OpenRouter)

- **Endpoint:** `POST /essay`
- **Functionality:** Generates an essay on a given topic using **DeepSeek**.
- **Example Request:**
  ```json
  {
    "topic": "money"
  }
  ```
- **Example Response:**
  ```json
  {
    "content": "Money plays a pivotal role in modern society, serving as a medium of exchange..."
  }
  ```

### Poem Generator (LLaMA-3 - Groq API)

- **Endpoint:** `POST /poem`
- **Functionality:** Generates a **child-friendly poem** about a given topic using **LLaMA-3**.
- **Example Request:**
  ```json
  {
    "topic": "ambition"
  }
  ```
- **Example Response:**
  ```json
  {
    "content": "Ambition is a shining light, guiding dreams both big and bright..."
  }
  ```

## Technologies Used

- **FastAPI** - API backend
- **Streamlit** - UI frontend
- **LangChain** - LLM integration
- **DeepSeek (via OpenRouter)** - Essay generation
- **LLaMA-3 (via Groq API)** - Poem generation

## Future Improvements

- Add support for more LLMs
- Improve UI design
- Implement user authentication

## Contributing

Feel free to fork the project and submit pull requests.

## License

MIT License

