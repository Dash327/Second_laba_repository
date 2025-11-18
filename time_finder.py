import re
import requests
import sys
import os

# Регулярное выражение для времени ЧЧ:ММ:СС
TIME_PATTERN = r"\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b"
TIME_REGEX = re.compile(TIME_PATTERN)
