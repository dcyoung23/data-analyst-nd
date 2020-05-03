import pandas as pd
import pandasql

df = pd.read_csv('final_data.csv')

position = df[df["Position"] == "C"]

# print position.describe()

optimal = df[df["Optimal"] == "Yes"]

# print optimal

q = """
select SeasonDay, Date, PlayerType
,SUM(Points) AS Points
,SUM(Salary) AS Salary
,COUNT(Player) AS Cnt
from optimal
group by SeasonDay, Date, PlayerType
"""

# Execute your SQL command against the pandas frame
optimal_data = pandasql.sqldf(q, locals())

output_filename = "optimal_data.csv"
optimal_data.to_csv(output_filename)
