import pandas as pd

def best(journal_df):
    condition = ((journal_df['maths'] >= 4) &
                 (journal_df['physics'] >= 4) &
                 (journal_df['computer science'] >= 4))

    filtered_df = journal_df[condition]
    return filtered_df

columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)

print(journal)
print(filtered)
