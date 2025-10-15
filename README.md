# 🤖 Finance Stock Advisor Multi-AI Agent

An intelligent multi-agent system powered by Google's Gemini AI and Phidata framework for comprehensive stock market analysis and financial insights.

## 📋 Overview

This project implements a sophisticated multi-agent AI system designed to provide expert financial analysis and stock market insights. It leverages multiple specialized AI agents working in coordination to deliver comprehensive financial advice, real-time market data, and intelligent recommendations.

### Key Features

- **Multi-Agent Architecture**: Utilizes specialized agents for different financial tasks
- **Real-Time Stock Data**: Integration with YFinance for live market data
- **Web Research Capabilities**: Uses DuckDuckGo for market research and news
- **Intelligent Analysis**: Powered by Google's Gemini 2.0 Flash model
- **Comprehensive Insights**: Combines technical analysis, fundamental data, and market sentiment

## 🏗️ Project Structure

```
FinanceStockAdvisorMultiAIAgent/
│
├── AgnoAIAgentFinal.ipynb    # Main Jupyter notebook with agent implementation
└── README.md                  # Project documentation (this file)
```

## 🔧 Requirements

Before running the project, ensure you have the following dependencies installed:

### Python Packages

```bash
pip install phidata
pip install google-generativeai
pip install yfinance
pip install duckduckgo-search
pip install openai  # For compatibility
```

### Environment Setup

1. **Google API Key**: You'll need a Google AI Studio API key
   - Get your API key from: https://aistudio.google.com/app/apikey
   - Set it as an environment variable or configure it in the notebook

2. **PHI_API_KEY** (Optional): For Phidata dashboard monitoring
   - Sign up at: https://phidata.app

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/Annamalai23/FinanceStockAdvisorMultiAIAgent.git
cd FinanceStockAdvisorMultiAIAgent
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install phidata google-generativeai yfinance duckduckgo-search openai
```

### Step 3: Configure API Keys

In the notebook, set your Google API key:

```python
import os
os.environ['GOOGLE_API_KEY'] = 'your-google-api-key-here'
```

### Step 4: Run the Notebook

1. Open Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```

2. Navigate to `AgnoAIAgentFinal.ipynb`

3. Run all cells sequentially

## 🤖 Agent Architecture

The system consists of specialized agents working together:

### 1. **Web Search Agent**
- Uses DuckDuckGo for web searches
- Gathers market news and financial information
- Provides context for investment decisions

### 2. **Finance Agent**
- Integrates with YFinance API
- Retrieves real-time stock prices and historical data
- Accesses company fundamentals and analyst recommendations
- Provides technical indicators

### 3. **Multi-Agent Team**
- Coordinates between specialized agents
- Combines insights from multiple sources
- Delivers comprehensive financial analysis

## 💡 Usage Examples

Once the notebook is running, you can interact with the agents:

### Example 1: Stock Analysis
```python
# Ask about stock performance
team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA",
    stream=True
)
```

### Example 2: Market Research
```python
# Get comprehensive market insights
team.print_response(
    "What are the current trends in AI chip manufacturers?",
    stream=True
)
```

### Example 3: Investment Advice
```python
# Request investment recommendations
team.print_response(
    "Should I invest in Tesla? Provide analysis with current data.",
    stream=True
)
```

## 🛠️ Technical Details

### Model Configuration
- **AI Model**: Google Gemini 2.0 Flash Experimental
- **Framework**: Phidata for agent orchestration
- **Data Sources**: 
  - YFinance for stock market data
  - DuckDuckGo for web research

### Agent Features
- **show_tool_calls**: Displays which tools are being used
- **markdown**: Formats responses in markdown
- **Streaming**: Real-time response streaming
- **Debug Mode**: Optional debugging for development

## 📊 What the System Can Do

✅ Real-time stock price analysis
✅ Company financial data retrieval
✅ Analyst recommendations summary
✅ Market news aggregation
✅ Technical indicator analysis
✅ Investment trend identification
✅ Multi-source data synthesis
✅ Natural language query processing

## 🔍 How It Works

1. **User Query**: Submit a financial question or request
2. **Agent Selection**: The system determines which agents to activate
3. **Data Collection**: Agents gather information from their respective sources
4. **Analysis**: AI model processes and analyzes collected data
5. **Synthesis**: Multi-agent team combines insights
6. **Response**: Comprehensive answer delivered to user

## 📝 Notes

- **API Rate Limits**: Be mindful of YFinance and Google API rate limits
- **Data Accuracy**: Stock data is real-time but subject to market delays
- **Investment Disclaimer**: This tool is for educational purposes. Always consult with a financial advisor before making investment decisions

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Annamalai23**
- GitHub: [@Annamalai23](https://github.com/Annamalai23)

## 🙏 Acknowledgments

- [Phidata](https://www.phidata.com/) for the agent framework
- [Google AI](https://ai.google.dev/) for Gemini AI model
- [YFinance](https://github.com/ranaroussi/yfinance) for financial data
- [DuckDuckGo](https://duckduckgo.com/) for web search capabilities

---

**⚠️ Disclaimer**: This is an educational project. The information provided by this system should not be considered as financial advice. Always do your own research and consult with qualified financial professionals before making investment decisions.
