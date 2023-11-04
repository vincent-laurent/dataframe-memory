from pandas._testing import makeTimeDataFrame
import numpy as np
from data_memory import reduce_memory, memory_usage
import pandas as pd

np.random.seed(0)


def test_time():
    df = makeTimeDataFrame(1000).reset_index()

    mem0 = memory_usage(df)
    reduce_memory(df, dates='index')
    mem1 = memory_usage(df)
    assert mem1 < mem0


def test_big_dataset_cat():
    df = pd.DataFrame(np.random.choice(['foo', 'bar', 'baz'], size=(1000, 3)))
    mem0 = memory_usage(df)
    reduce_memory(df)
    mem1 = memory_usage(df)
    for c in df.columns:
        assert df[c].dtypes.name == "category"
    assert mem1*30 < mem0
