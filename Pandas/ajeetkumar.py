import pandas as pd

data = {
    'Team': ['Red', 'Blue', 'Red', 'Blue', 'Red'],
    'Score': [5, 7, 3, 8, 6],
    'Player': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

grouped = df.groupby('Team')

mean_score = grouped['Score'].mean()
print(mean_score)
