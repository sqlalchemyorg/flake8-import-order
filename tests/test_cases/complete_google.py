from __future__ import absolute_import

import ast
from functools import *
import os
from os import path
import sys

import flake8_import_error
from flake8_import_error import *
import X
from X import *
from X import A
from X import b, C, d
import Y
from Y import *
from Y import A
from Y import B, C, D
import Z
from Z import A
from Z.A import A
from Z.A.B import A

from . import A
from . import B
from .A import A
from .B import B
from .. import A
from .. import B
from ..A import A
from ..B import B
