#!/bin/sh

# Ensure the script exits if any command fails
set -e

# Check if a virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Warning: No virtual environment detected. Make sure to activate your virtual environment before running the script."
  echo "Press any key to continue or Ctrl+C to cancel..."
  read -n 1 -s
fi

# Set the Django settings module to the test settings
export DJANGO_SETTINGS_MODULE=daelibs_interview.settings.test

# Print an informational message
echo "Running tests with DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}..."

# Use 'env' to locate the Python interpreter
if command -v python3 &>/dev/null; then
  PYTHON_CMD=python3
elif command -v python &>/dev/null; then
  PYTHON_CMD=python
else
  echo "Error: Python interpreter not found."
  exit 1
fi

# Run the tests
$PYTHON_CMD manage.py test

# Print a completion message
echo "Tests completed."