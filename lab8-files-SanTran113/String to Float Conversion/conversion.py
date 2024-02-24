# Name: San Tran
# Date: 11 / 9 / 22
# GitHub: SanTran113
from typing import Optional


def stringToFloat(in_: str) -> Optional[float]:
    try:
        line = float(in_)
        return line
    except ValueError:
        return None

# else:
#     print(None)
