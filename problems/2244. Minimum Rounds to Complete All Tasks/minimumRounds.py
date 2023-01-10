import pandas as pd

def minimumRounds(tasks: list[int]) -> int:
    ''' It uses Pandas, but LeedCode doesn't support it '''
    result = 0
    tasks_series = pd.Series(tasks)
    tasks_set = tasks_series.unique()
    counts = tasks_series.value_counts()

    for i in tasks_set:
        if counts.get(i) <= 1:
            return -1
        else:
            result += counts.get(i) // 3 + (counts.get(i) % 3 > 0)

    return result

print(minimumRounds([2,2,3,3,2,4,4,4,4,4])) # 4
print(minimumRounds([2,3,3])) # -1