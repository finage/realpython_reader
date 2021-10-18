FROM python
RUN python -m pip install twine feedparser html2text
WORKDIR /app
