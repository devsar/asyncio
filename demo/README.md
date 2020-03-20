Use python 3.9-dev or superior

# Notes
Management suggests the use of:

- Pyenv (for virtualenv creation and python activation)


# Test it

curl -o /dev/null -w  "%{time_starttransfer}\n" http://localhost:8000/slow/

curl -o /dev/null -w  "%{time_starttransfer}\n" http://localhost:8000/fast/

