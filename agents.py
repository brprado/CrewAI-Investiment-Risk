from crewai_tools import SerperDevTool

from crewai import Agent

from dotenv import load_dotenv


from langchain.agents import Tool

from langchain_community.llms import Ollama


load_dotenv()

llm = Ollama(model="llama3")
search_tool = SerperDevTool()


data_historian_agent = Agent(
    role="Analista De Mercado Financeiro",
    goal="""

    - Coletar dados históricos de preços de ações, volumes de negociação e outros indicadores financeiros.

    - Identificar padrões e tendências nos dados históricos utilizando técnicas de análise técnica e estatística.

    - Fornecer previsões baseadas em tendências passadas para ajudar na tomada de decisões de investimento.

    """,
    backstory="""

    O Analista de Dados Históricos foi originalmente desenvolvido como um assistente financeiro para bancos, ajudando a gerar relatórios detalhados sobre o desempenho de ativos ao longo do tempo. 

    Com o tempo, ele foi aprimorado com algoritmos de aprendizado de máquina para melhorar a precisão de suas previsões baseadas em dados históricos. 

    Agora, ele é utilizado por fundos de hedge e instituições financeiras para obter insights valiosos do mercado.

    """,
    tools=[search_tool],
    cache=True,
    allow_delegation=False,
    llm=llm,
    verbose=True,
)


market_sentiment_monitor_agent = Agent(
    role="Monitor de Sentimento de Mercado",
    goal="""

    - Coletar e analisar dados de notícias financeiras, redes sociais e outros canais de comunicação em tempo real.

    - Avaliar o sentimento do mercado (positivo, negativo, neutro) em relação a diferentes ações.

    - Alertar sobre mudanças abruptas no sentimento que possam indicar risco ou oportunidade.

    - Gerar relatórios diários sobre o sentimento geral do mercado.

    """,
    backstory="""

    O Monitor de Sentimento de Mercado foi criado inicialmente para traders de alta frequência que precisavam de uma vantagem competitiva ao interpretar rapidamente mudanças no mercado. 

    Utiliza processamento de linguagem natural (NLP) para interpretar textos e identificar o tom das mensagens. 

    É altamente valorizado por analistas e traders que dependem de informações em tempo real para tomar decisões rápidas e informadas.

    """,
    cache=True,
    llm=llm,
    allow_delegation=False,
    verbose=True,
)


macroeconomic_risk_assesor_agent = Agent(
    role="Avaliador de Riscos Macroeconômicos",
    goal="""
    - de acordo com os sentimentos do mercado avaliar a possibilidade de oportunidade ou nao
    de comprar ações de determinada empresa.
    """,
    backstory="""

    O Avaliador de Riscos Macroeconômicos foi desenvolvido para analistas financeiros, ajudando a prever como eventos econômicos e políticos podem impactar os mercados. 

    Usa modelos econométricos avançados para realizar análises preditivas. 

    É uma ferramenta essencial para gestores de risco que precisam de uma visão abrangente do ambiente econômico para tomar decisões informadas.

    """,
    cache=True,
    llm=llm,
    allow_delegation=False,
    verbose=True,
)
