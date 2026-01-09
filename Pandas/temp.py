import pandas as pd

store_data = pd.DataFrame({
    'Category': ['Electronics', 'Clothing', 'Grocery', 'Electronics', 'Clothing',
                 'Grocery', 'Electronics', 'Clothing', 'Grocery', 'Electronics'],
    'Store': ['Store_A', 'Store_B', 'Store_C', 'Store_A', 'Store_B',
              'Store_C', 'Store_A', 'Store_B', 'Store_C', 'Store_A'],
    'Sales': [5000, 3000, 1500, 7000, 4000,
              2000, 6500, 3500, 1800, 8000]
})

print(
    store_data
    .groupby(['Category', 'Store'], as_index=False)['Sales']
    .sum()
)

result = store_data.groupby(['Category','Store'])['Sales'].sum().reset_index()
print(type(result))

