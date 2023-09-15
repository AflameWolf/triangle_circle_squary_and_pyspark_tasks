from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("pyspark_task").getOrCreate()

category = spark.createDataFrame([
    (1, "Category 1"),
    (2, "Category 2"),
    (3, "Category 3"),
    (4, "Category 4"),
    (5, "Category 5"),
    (6, "Category 6"),],
    ["id", "category_name"],
)

product= spark.createDataFrame([
    (1, "Product 1"),
    (2, "Product 2"),
    (3, "Product 3"),
    (4, "Product 4"),
    (5, "Product 5"),
    (6, "Product 6"),
    (7, "Product 7"),
    (8, "Product 8"),
    (9, "Product 9"),
    (10, "Product 10"),
    (11, "Product 11"), ],  # Продукт без категории
    ["id", "product_name", ]
)


product_category = spark.createDataFrame([
    (1, 1),
    (2, 3),
    (3, 2),
    (3, 4),
    (6, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (4, 2),
    (1, 8),
    (4, 9),
    (1, 10)],
    ["category_id", "product_id", ]
)




query = ( product.join(product_category,product.id == product_category.product_id, how='left')
            .join(category,product_category.category_id == category.id, how='left').select(['category_name', 'product_name'])
)


query.orderBy("category_id").show()
