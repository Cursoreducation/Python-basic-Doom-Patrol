import os
import inspect
from datetime import datetime

operations = {1: ["add", "+"],
              2: ["subtract", "-"],
              3: ["multiply", "*"],
              4: ["divide", "/"],
              5: ["power by", "**"],
              6: ["stop", False]}