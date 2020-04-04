#!/bin/bash

if [ ${#BASH_SOURCE[@]} -eq 1 ] && [ ${BASH_SOURCE[0]} = ${0} ]; then
  echo "Stop! Please try \`source ${0}\` instead."
  exit 1
fi

PROJECT_ROOT=$(cd `dirname $BASH_SOURCE[0]` | pwd)
export PROJECT_ROOT


# activate virtual environment
. venv/bin/activate

# setup environment variables for flask
export FLASK_APP=application.py
export FLASK_ENV=development

# setup database uri needed for app
export DATABASE_URI=mysql+pymysql://localhost/shopar

# load aliases for convenience if exists
FILE_DIR=$(dirname "${BASH_SOURCE}")
ALIASES="${FILE_DIR}/.aliases"
if [ -e "$ALIASES" ]; then
  source "$ALIASES"
fi

# use python setup script if exists
PYTHONSTARTUP_FILE="${FILE_DIR}/.pythonstartup"
if [ -e "${PYTHONSTARTUP_FILE}" ]; then
  export PYTHONSTARTUP="${PYTHONSTARTUP_FILE}"
fi

# use local environment file to overwrite if exists
LOCAL_ENV=${PROJECT_ROOT}/.env
if [ -e ${LOCAL_ENV} -a -f ${LOCAL_ENV} ]; then
  source ${LOCAL_ENV}
fi
