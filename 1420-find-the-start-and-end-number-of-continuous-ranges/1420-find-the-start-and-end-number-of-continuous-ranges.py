import pandas as pd

import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values("log_id",ignore_index=True) #logs_id in testcases are sorted, but just in case
    return logs.groupby(logs.log_id-logs.index).agg(start_id=("log_id","min"),end_id=("log_id","max"))
  