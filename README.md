# PPTGenerator

PPTGenerator is a powerful tool that creates professional presentations from user input. It offers flexibility to include or exclude code snippets in your slides and lets you choose your preferred LLM (Large Language Model) for content generation.

## Features

- Generate complete PowerPoint presentations from simple text prompts
- Option to include or exclude code snippets in your slides
- Choose your preferred LLM (Gemini, Grok, or ChatGPT)
- Integration with Pexels API for high-quality images
- Modern web interface built with Tailwind CSS

## Prerequisites

Before using PPTGenerator, you'll need API keys for the following services:

- Gemini AI
- Grok API
- OpenAI (ChatGPT)
- Pexels API

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/pptgenerator.git
cd pptgenerator
```

2. Create a `project.env` file in the root directory with your API keys:
```
GEMINI_API_KEY=your_gemini_api_key
GROK_API_KEY=your_grok_api_key
OPENAI_API_KEY=your_chatgpt_api_key
PEXELS_API_KEY=your_pexels_api_key
```

3. Install Python dependencies:
```
pip install -r requirements.txt
```

4. Install frontend dependencies:
```
npm install tailwindcss @tailwindcss/vite
cd PPT-GEN
npm install
```

## Usage

1. Start the Python backend:
```
python3 pptgen.py
```

2. In a new terminal, start the frontend development server:
```
cd PPT-GEN
npm run dev
```

3. Open your browser and navigate to `http://localhost:5173` (or the port specified in the terminal)

4. Enter your presentation topic, choose your preferred LLM, and specify whether to include code snippets

5. Click "Generate" and wait for your presentation to be created

## How It Works

PPTGenerator leverages the power of Large Language Models to create structured, informative presentations. The backend processes your request, generates content using your chosen LLM, and formats it into a PowerPoint presentation. If enabled, the system will intelligently include and format code snippets relevant to your topic.

## Troubleshooting

- **API Key Issues**: Ensure your API keys in the `project.env` file are correct and have the necessary permissions
- **Backend Connection Error**: Make sure the Python backend is running before starting the frontend
- **Missing Dependencies**: Run `pip install -r requirements.txt` and check for any errors

