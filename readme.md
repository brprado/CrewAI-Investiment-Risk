# Financial Market Analysis Agents

## Overview

This project consists of three specialized AI agents designed to assist in financial market analysis. Each agent has a unique role and set of goals to provide comprehensive insights into various aspects of the financial market.

## Agents

1. **Data Historian Agent**
2. **Market Sentiment Monitor Agent**
3. **Macroeconomic Risk Assessor Agent**

## Agent Details

### Data Historian Agent

- **Role**: Financial Market Analyst
- **Goal**:
  - Collect historical data on stock prices, trading volumes, and other financial indicators.
  - Identify patterns and trends in historical data using technical and statistical analysis techniques.
  - Provide forecasts based on past trends to aid in investment decision-making.
- **Backstory**:
  - Originally developed as a financial assistant for banks, generating detailed reports on asset performance over time.
  - Enhanced with machine learning algorithms to improve prediction accuracy based on historical data.
  - Now used by hedge funds and financial institutions to gain valuable market insights.

### Market Sentiment Monitor Agent

- **Role**: Market Sentiment Monitor
- **Goal**:
  - Collect and analyze data from financial news, social media, and other communication channels in real-time.
  - Assess market sentiment (positive, negative, neutral) regarding different stocks.
  - Alert about abrupt changes in sentiment that may indicate risk or opportunity.
  - Generate daily reports on the overall market sentiment.
- **Backstory**:
  - Initially created for high-frequency traders who needed a competitive edge by quickly interpreting market changes.
  - Utilizes natural language processing (NLP) to interpret texts and identify the tone of messages.
  - Highly valued by analysts and traders who rely on real-time information to make quick, informed decisions.

### Macroeconomic Risk Assessor Agent

- **Role**: Macroeconomic Risk Assessor
- **Goal**:
  - Evaluate the potential opportunity or risk of buying a company's stock based on market sentiment.
- **Backstory**:
  - Developed for financial analysts to predict how economic and political events might impact markets.
  - Uses advanced econometric models for predictive analysis.
  - Essential for risk managers who need a comprehensive view of the economic environment to make informed decisions.

## How to Run the Project

### Requirements

- [X] Python 3.8+
- [X] Dependencies listed in `requirements.txt`
- [X] SERPER_API_KEY on the .env file

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/brprado/CrewAI-Investiment-Risk.git
   cd CrewAI-Investiment-Risk
   ```
2. Install requirements.txt

   ```
   pip install -r requirements.txt
   ```
3. Run the project

   ```python
   python crew.py
   ```
