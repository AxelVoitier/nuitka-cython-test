FROM python:3.7.6-slim-buster

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc g++
RUN pip --no-cache-dir install Cython==0.29.14

# RUN pip --no-cache-dir install nuitka==0.6.4  # Working
RUN pip --no-cache-dir install nuitka==0.6.7  # ImportError
# RUN pip --no-cache-dir install https://github.com/Nuitka/Nuitka/archive/develop.zip  # ImportError

COPY fib-package/ /app/fib-package/
WORKDIR /app

RUN pip install fib-package/
RUN nuitka3 --show-progress --recurse-all /usr/local/bin/fib

CMD ["/app/fib.bin"]
