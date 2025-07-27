import pandas as pd

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    # 1) 시험별로 최소/최대 점수 계산
    bounds = (
        exam
        .groupby('exam_id', as_index=False)['score']
        .agg(min_score='min', max_score='max')
    )
    
    # 2) exam에 합쳐서, 각 응시마다 '내 점수가 min/max인지' 표시
    merged = exam.merge(bounds, on='exam_id')
    merged['is_extreme'] = (
        (merged['score'] == merged['min_score']) |
        (merged['score'] == merged['max_score'])
    )
    
    # 3) 한 번이라도 min/max 받은 student_id 집합
    extreme_ids = merged.loc[merged['is_extreme'], 'student_id'].unique()
    
    # 4) 시험을 본 student_id 집합
    took_exam_ids = exam['student_id'].unique()
    
    # 5) quiet student_id: 시험도 봤고, extreme_ids에 없고
    quiet_ids = [sid for sid in took_exam_ids if sid not in extreme_ids]
    
    # 6) student DataFrame에서 필터링 & 정렬
    return (
        student[student['student_id'].isin(quiet_ids)]
        .sort_values('student_id')
        .reset_index(drop=True)
    )