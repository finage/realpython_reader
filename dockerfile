FROM python
RUN python -m pip install twine feedparser html2text
RUN pip install -i https://test.pypi.org/simple/ $PACKAGE_NAME==$version
