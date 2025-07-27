import pandas as pd

import pandas as pd

import pandas as pd

def most_frequently_products(customers: pd.DataFrame,
                             orders: pd.DataFrame,
                             products: pd.DataFrame) -> pd.DataFrame:
    # 1. Orders와 Products를 조인해 product_name까지 붙임
    df = orders.merge(products, on='product_id', how='inner')
    
    # 2. 고객-상품별 주문 횟수를 집계
    grouped = df.groupby(['customer_id', 'product_id', 'product_name']).size().reset_index(name='cnt')
    # grouped 예시:
    # customer_id | product_id | product_name | cnt

    # 3. 고객별 최대 주문 횟수를 구함
    max_df = grouped.groupby('customer_id', as_index=False)['cnt'].max()
    max_df = max_df.rename(columns={'cnt': 'max_cnt'})
    # max_df 예시:
    # customer_id | max_cnt

    # 4. grouped과 max_df를 customer_id로 merge
    merged = grouped.merge(max_df, on='customer_id')
    # merged 예시:
    # customer_id | product_id | product_name | cnt | max_cnt

    # 5. cnt == max_cnt 인 행만 필터링
    result = merged[merged['cnt'] == merged['max_cnt']][['customer_id','product_id','product_name']].reset_index(drop=True)

    return result