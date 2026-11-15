if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    unique_scores = sorted(set(score for name, score in records))
    second_lowest_score = unique_scores[1]

    second_lowest_students = sorted(
        name for name, score in records if score == second_lowest_score
    )

    for name in second_lowest_students:
        print(name)
