import pandas as pd

import pandas as pd

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    # 1) 초기: CEO에게 직접 보고하는 직원들
    # manager_id가 1번이고, employee_id != 1인 직원
    result = set(employees.loc[(employees['manager_id'] == 1) & (employees['employee_id'] != 1), 'employee_id'])
    
    # 2) 현재 단계에서 찾은 직원들이 다음 단계에서 manager가 된다
    current = result.copy()
    
    # 3) 더 이상 새로운 직원이 없을 때까지 반복
    while current:
        # 현재 current 리스트를 매니저로 갖는 직원 찾기
        next_level = set(employees.loc[employees['manager_id'].isin(current), 'employee_id'])
        # 새로 찾은 직원들 중 기존에 없는 것만 추가
        new = next_level - result
        if not new:
            break
        result.update(new)
        current = new  # 다음 루프에서 이들을 매니저로 탐색
    
    # 4) 결과를 DataFrame으로 변환
    return pd.DataFrame(sorted(result), columns=['employee_id'])    