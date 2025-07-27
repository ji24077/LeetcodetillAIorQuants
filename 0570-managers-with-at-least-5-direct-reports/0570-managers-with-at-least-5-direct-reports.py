import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # managerId별 부하직원 수 세기 (groupby 후 size → Series)
    counts = employee.groupby('managerId').size()

    # 부하직원이 5명 이상인 managerId만 추출
    mgr_ids = counts[counts >= 5].index

    # employee에서 id가 그 managerId인 사람들의 이름만 선택
    return employee[employee['id'].isin(mgr_ids)][['name']]