# conftest.py
import os
import sys
import pytest

sys.path.append(os.path.abspath("./"))
os.environ["TEST_ROOT"] = os.path.abspath("./tests")
