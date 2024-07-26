from flask import *

from typing import *

type strbool = Union[bool, str]
# тип, служащий ответом для функций-фильтраторов данных

app = Flask(__name__)