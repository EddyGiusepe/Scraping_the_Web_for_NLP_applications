#! /usr/bin/env python
"""
Senior Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Script scrape_any_website_with_nlp.py
=====================================
ScrapeGraphAI é uma biblioteca de Python para extrair dados de
qualquer site da web usando `LLMs`.

Run
---
uv run scrape_any_website_with_nlp.py
"""

import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel, Field
from scrapegraphai.graphs import SmartScraperGraph

_ = load_dotenv(find_dotenv())  # read local .env file
# openai.api_key  = os.environ['OPENAI_API_KEY']
Eddy_key_openai = os.environ["OPENAI_API_KEY"]


class Book(BaseModel):
    title: str = Field(description="Book title")
    price: str = Field(description="Book price with currency symbol")


class BooksResult(BaseModel):
    books: list[Book] = Field(
        description="List of extracted books with their respective prices"
    )


graph_config = {
    "llm": {
        "api_key": Eddy_key_openai,
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

smart_scraper = SmartScraperGraph(
    prompt="Extract the first 5 book titles and their prices",
    source="https://books.toscrape.com",
    config=graph_config,
    schema=BooksResult,
)

result = smart_scraper.run()
print(result)

"""
{'books': [{'title': 'A Light in the Attic', 'price': '£51.77'},
           {'title': 'Tipping the Velvet', 'price': '£53.74'},
           {'title': 'Soumission', 'price': '£50.10'},
           {'title': 'Sharp Objects', 'price': '£47.82'},
           {'title': 'Sapiens: A Brief History of Humankind', 'price': '£54.23'}]}
"""
