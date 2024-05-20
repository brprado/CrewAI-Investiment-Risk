from crewai import Agent, Task, Crew
from agents import (
    data_historian_agent,
    market_sentiment_monitor_agent,
    macroeconomic_risk_assesor_agent,
)


historical_data_search_task = Task(
    description="""
    Procure na internet por dados históricos de preços de ações, volumes de negociação e outros indicadores financeiros relevantes da empresa {empresa}.
    Foque em obter dados de pelo menos cinco anos para realizar uma análise detalhada.
    Utilize fontes confiáveis como Yahoo Finance, Google Finance, ou sites oficiais de bolsas de valores.
    """,
    expected_output="""
    UM texto sumarizado que informe claramente as tendencias desta empresa
    """,
    agent=data_historian_agent,
)

market_sentiment_task = Task(
    description="""
    Monitore e analise dados de notícias financeiras, redes sociais e outros canais de comunicação em tempo real sobre a empresa {empresa}.
    Avalie o sentimento do mercado (positivo, negativo, neutro) em relação às ações da {empresa}.
    Gere alertas sobre mudanças abruptas no sentimento que possam indicar risco ou oportunidade.
    """,
    expected_output="""
    A partir das noticias e informacoes do mercado analise o sentimento geral sobre a {empresa}
    """,
    agent=market_sentiment_monitor_agent,
)

risk_assesor_task = Task(
    description="""
    Avalie os riscos macroeconômicos que podem impactar a empresa {empresa}.
    Analise dados de PIB, taxa de desemprego, inflação, políticas monetárias, e eventos políticos.
    Forneça previsões sobre possíveis impactos econômicos e políticos nos mercados financeiros e como eles podem afetar a {empresa}.
    """,
    expected_output="""
    Um relatório de avaliação de riscos para {empresa} com:
    - Explicacao do por que investir
    - Riscos de investir
    - Decisao final (Comprar ou Nao)
    """,
    agent=macroeconomic_risk_assesor_agent,
    output_file="stock_risk.md",
)
