import pandas as pd


def most_recent_orders(customers: pd.DataFrame, 
                       orders: pd.DataFrame, 
                       products: pd.DataFrame) -> pd.DataFrame:
    # 1) 각 product_id 별로 가장 최근 날짜(max_date)를 구한다
    max_dates = orders.groupby('product_id', as_index=False)['order_date'].max()
    # max_dates 예시:
    # product_id | order_date
    #     1      | 2020-08-01
    #     2      | 2020-08-03
    #     3      | 2020-08-29

    # 2) 원래 주문 데이터(orders)와 max_dates를 product_id와 order_date로 매칭
    merged = orders.merge(max_dates, on=['product_id', 'order_date'])
    # merged에는 각 제품별 최신날짜에 해당하는 주문만 남음

    # 3) 제품 이름을 붙이기 위해 products와 조인
    merged = merged.merge(products, on='product_id')
    # merged 예시:
    # product_id | order_id | order_date | product_name

    # 4) 최종 컬럼 선택 및 정렬
    result = merged[['product_name', 'product_id', 'order_id', 'order_date']]
    result = result.sort_values(['product_name', 'order_id']).reset_index(drop=True)

    return result
    