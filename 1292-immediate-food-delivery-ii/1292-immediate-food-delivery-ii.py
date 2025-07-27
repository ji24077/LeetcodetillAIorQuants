import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # 고객별 가장 첫 주문만 남김
    first_orders = delivery.sort_values('order_date').groupby('customer_id').first()

    # 전체 고객 수
    total = len(first_orders)

    # 첫 주문이 즉시배송인 고객 수
    immediate = (first_orders['order_date'] == first_orders['customer_pref_delivery_date']).sum()

    # 비율 계산
    immediate_percentage = round(immediate / total * 100, 2)

    return pd.DataFrame({'immediate_percentage':[immediate_percentage]})    