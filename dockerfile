FROM python
ENV package_name=${PACKAGE_NAME}
ENV version=${version}
RUN python -m pip install twine feedparser html2text
RUN pip install -i https://test.pypi.org/simple/ package_name==version
