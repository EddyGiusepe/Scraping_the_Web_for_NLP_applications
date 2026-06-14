#! /usr/bin/env python
"""
Senior Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Script basic_usage.py
=====================
Este script demonstra o uso básico da biblioteca Scrapling para
fazer uma requisição HTTP, simular um navegador Chrome e extrair
conteúdo específico de uma página web usando seletores CSS.
"""

from scrapling.fetchers import FetcherSession

with FetcherSession(
    impersonate="chrome"
) as session:  # Use latest version of Chrome's TLS fingerprint
    page = session.get("https://quotes.toscrape.com/", stealthy_headers=True)
    quotes = page.css(".quote .text::text").getall()
    # print(quotes)
    for quote in quotes:
        print(quote)


# Or use one-off requests
# page = Fetcher.get('https://quotes.toscrape.com/')
# quotes = page.css('.quote .text::text').getall()
# for quote in quotes:
#    print(quote)
