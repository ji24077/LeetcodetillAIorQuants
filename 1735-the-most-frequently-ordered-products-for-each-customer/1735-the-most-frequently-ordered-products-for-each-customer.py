import pandas as pd

import pandas as pd

def most_frequently_products(customers: pd.DataFrame,
                             orders: pd.DataFrame,
                             products: pd.DataFrame) -> pd.DataFrame:
    # 1. Orders와 Products를 merge하여 product_name 붙이기
    df = orders.merge(products, on='product_id', how='inner')
    # 2. 고객 ID로 groupby할 수 있게 유지
    #    (customers와는 나중에 필요하면 join 가능하지만 여기선 주문이 있는 고객만)
    
    # 3. 고객-상품별로 주문 횟수 집계
    grouped = df.groupby(['customer_id','product_id','product_name']).size().reset_index(name='cnt')
    
    # 4. 각 customer_id별로 최대 주문 횟수 구하기
    max_cnts = grouped.groupby('customer_id')['cnt'].transform('max')
    
    # 5. 최대 주문 횟수와 동일한 행만 필터
    result = grouped[grouped['cnt'] == max_cnts][['customer_id','product_id','product_name']].reset_index(drop=True)
    
    return result