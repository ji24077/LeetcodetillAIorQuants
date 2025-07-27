import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
   # logs는 log_id 하나의 컬럼만 있다고 가정
    logs = logs.sort_values('log_id')  # 정렬
    
    start = None
    end = None
    ranges = []  # 결과 저장 리스트
    
    # 순차적으로 비교
    prev = None
    for x in logs['log_id']:
        if prev is None or x != prev + 1:  # 불연속이면 새로운 구간 시작
            if start is not None:
                ranges.append((start, end))  # 이전 구간 저장
            start = x
            end = x
        else:
            end = x  # 연속이면 end 갱신
        prev = x
    # 마지막 구간 추가
    if start is not None:
        ranges.append((start, end))
    
    return pd.DataFrame(ranges, columns=['start_id','end_id'])