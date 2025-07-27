import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # seat을 복사해서 결과를 담음
    result = seat
    
    # 짝수행(인덱스 1,3,5…)과 홀수행(인덱스 0,2,4…) swap
    for i in range(0, len(seat)-1, 2):
        result.loc[i, 'student'], result.loc[i+1, 'student'] = seat.loc[i+1, 'student'], seat.loc[i, 'student']
    
    return result    