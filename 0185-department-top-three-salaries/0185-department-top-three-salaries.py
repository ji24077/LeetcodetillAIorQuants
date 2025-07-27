import pandas as pd

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 1) 부서명 붙이기 (JOIN)
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp','_dept'))
    # merged에는 name_emp(직원 이름), salary, name_dept(부서명) 등이 포함됨

    # 2) 각 부서별 salary 기준 내림차순 dense rank
    merged['rnk'] = merged.groupby('departmentId')['salary'].rank(method='dense', ascending=False)

    # 3) 상위 3명만 남기기
    top3 = merged[merged['rnk'] <= 3]

    # 4) 정렬: 부서명 오름차순, salary 내림차순
    top3 = top3.sort_values(by=['name_dept', 'salary'], ascending=[True, False])

    # 5) 원하는 컬럼만 남기고 이름 변경
    result = top3[['name_dept', 'name_emp', 'salary']].copy()
    result.columns = ['Department', 'Employee', 'Salary']

    return result

