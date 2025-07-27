import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # pandas에서 조건 필터링: SQL WHERE 절과 동일
    filtered = products[(products['low_fats'] == 'Y')
     & (products['recyclable'] == 'Y')]
    
    # 필요한 컬럼만 선택
    return filtered[['product_id']]    