import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 1) 부서별 최대 연봉을 구한다
    max_salary = employee.groupby('departmentId', as_index=False)['salary'].max()
    max_salary = max_salary.rename(columns={'salary': 'max_salary'})
    # max_salary 예시:
    # departmentId | max_salary
    # 1            | 90000
    # 2            | 80000

    # 2) employee 테이블과 조인해서 해당 부서의 최대 연봉자만 필터링
    merged = employee.merge(max_salary,
                            on='departmentId',
                            how='inner')
    filtered = merged[merged['salary'] == merged['max_salary']]
    # filtered 예시:
    # id | name | salary | departmentId | max_salary
    # 2  | Jim  | 90000  | 1            | 90000
    # 5  | Max  | 90000  | 1            | 90000
    # 3  | Henry| 80000  | 2            | 80000

    # 3) 부서 이름 붙이기
    result = filtered.merge(department,
                            left_on='departmentId',
                            right_on='id',
                            how='inner')

    # 4) 컬럼 정리
    result = result[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    return result