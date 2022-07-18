if __name__ == '__main__':
    sn, second_lowest_score = [], 0
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        sn.append((score, name))
    second_lowest_score = sorted(
        {s[0] for s in sn}
    )[1]
    print('\n'.join(sorted((s[1] for s in sn if s[0]==second_lowest_score))))
