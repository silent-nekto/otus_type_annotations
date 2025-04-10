from typing import Never
import sys


def stop() -> Never:
    sys.exit(1)

