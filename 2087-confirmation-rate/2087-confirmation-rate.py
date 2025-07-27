import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # 전체 요청 수와 confirmed=true 수를 동시에 집계
  total = confirmations.groupby('user_id').size()
  confirmed = confirmations[confirmations['action'] == 'confirmed'].groupby('user_id').size()
  rate = (confirmed / total).fillna(0).round(2)
  result = signups[['user_id']]
  result['confirmation_rate'] = result['user_id'].map(rate).fillna(0)
  return result