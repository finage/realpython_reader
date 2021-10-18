FROM python as tmp_image
ARG version 
ARG package_name
RUN python -m pip install twine feedparser html2text
RUN pip install -i https://test.pypi.org/simple/ "$package_name"=="$version"
