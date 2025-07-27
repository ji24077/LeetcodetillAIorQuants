import pandas as pd

import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # 1. 프로젝트와 직원 정보를 한 번에 합친다 (INNER JOIN)
    merged = project.merge(employee, on='employee_id')  
    # merged 컬럼: project_id, employee_id, name, experience_years

    # 2. 각 project_id별 최대 경력 값을 구한다
    max_exp = merged.groupby('project_id')['experience_years'].max().reset_index()
    # max_exp: project_id, experience_years(최대값)

    # 3. 최대 경력값과 매칭되는 행만 필터링
    result = merged.merge(max_exp, on=['project_id', 'experience_years'])

    # 4. 컬럼 순서 정리
    return result[['project_id', 'employee_id']]