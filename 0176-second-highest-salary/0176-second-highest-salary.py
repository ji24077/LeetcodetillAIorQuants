import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # salary 컬럼의 중복 제거 후 정렬
    unique_salaries = sorted(employee['salary'].unique(), reverse=True)
    # 두 번째로 높은 급여가 있는지 확인
    if len(unique_salaries) < 2:
        # 두 번째 급여가 없으면 None 반환
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        # 두 번째로 높은 급여 반환
        return pd.DataFrame({'SecondHighestSalary': [unique_salaries[1]]})