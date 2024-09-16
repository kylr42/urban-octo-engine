from prometheus_client import Counter

products_created_total = Counter(
    'products_created_total',
    'Общее количество созданных продуктов'
)

total_product_price = Counter(
    'total_product_price',
    'Общая цена всех продуктов'
)
