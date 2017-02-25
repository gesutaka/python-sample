"""
型アノテーションサンプル
"""

from typing import List
import pandas as pd


# 関数編
def sample(x: str, y: int, z: pd.DataFrame) -> List[pd.DataFrame]:
    print(x.lower())
    print(y.bit_length())
    print(z.reset_index())

    return [pd.DataFrame()]

result = sample('x', 2, pd.DataFrame())
result[0].reset_index()  # reset_index部分に補完効く


# 変数編
dummy1 = ""  # type: pd.DataFrame
dummy1.reset_index()  # アノテーションが優先され、reset_indexの補完が効く

dummy = []  # type: List[pd.DataFrame]
dummy[0].reset_index()  # listの中身でも補完効く
