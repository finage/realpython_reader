FROM python as tmp_image
ARG version 
ARG package_name
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN python -m pip install twine feedparser html2text
RUN echo "package name is - $package_name"
RUN echo "version is - $version"
RUN pip install -v -i https://test.pypi.org/simple/ "$package_name"=="$version"
