FROM python:3.6.5
# -- Install Pipenv:
RUN pip install pipenv --upgrade
WORKDIR /tmp

# -- Adding Pipfiles
ADD ./Pipfile Pipfile
ADD ./Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --system
