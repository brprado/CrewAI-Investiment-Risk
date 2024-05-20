from deep_translator import GoogleTranslator
from crewai import Process, Crew
from agents import (
    data_historian_agent,
    market_sentiment_monitor_agent,
    macroeconomic_risk_assesor_agent,
)
from tasks import historical_data_search_task, market_sentiment_task, risk_assesor_task

crew = Crew(
    agents=[
        data_historian_agent,
        market_sentiment_monitor_agent,
        macroeconomic_risk_assesor_agent,
    ],
    tasks=[historical_data_search_task, market_sentiment_task, risk_assesor_task],
    process=Process.sequential,  # Executar tarefas em sequência
)


def translate_md(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    translator = GoogleTranslator(source="en", target="pt")
    translated_content = translator.translate(content)

    with open("risco_acoes.md", "w", encoding="utf-8") as file:
        file.write(translated_content)

    print("A tradução foi concluída e salva em 'risco_acoes.md'.")


if __name__ == "__main__":
    empresa = str(input("Sobre qual empresa voce quer verificar o risco?"))
    result = crew.kickoff(inputs={"empresa": empresa})
    translate_md("stock_risk.md")
