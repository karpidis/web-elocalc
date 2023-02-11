table_pd = [[0, 0.5], [3, 0.5], [10, 0.51], [17, 0.52], [25, 0.53], [32, 0.54], [39, 0.55], [46, 0.56],
            [53, 0.57], [61, 0.58], [68, 0.59], [76, 0.6], [83, 0.61], [91, 0.62], [98, 0.63], [106, 0.64],
            [113, 0.65], [121, 0.66], [129, 0.67], [137, 0.68], [145, 0.69], [153, 0.7], [162, 0.71], [170, 0.72],
            [179, 0.73], [188, 0.74], [197, 0.75], [206, 0.76], [215, 0.77], [225, 0.78], [235, 0.79], [245, 0.8],
            [256, 0.81], [267, 0.82], [278, 0.83], [290, 0.84], [302, 0.85], [315, 0.86], [328, 0.87], [344, 0.88],
            [357, 0.89], [374, 0.9], [391, 0.91], [411, 0.92], [432, 0.93], [456, 0.94], [484, 0.95], [517, 0.96],
            [559, 0.97], [619, 0.98], [735, 0.99], [10000, 1]]
rows = len(table_pd)


def difr400(elo1: int, elo2: int, result: float, k: int) -> float:
    """(int,int,float,int) -> float
    Return rating difference base on 2 players ratings, result and development coefficient.

    >>> difr(1500, 1500, 0.5, 20)
    0.0
    >>> difr(1600, 1725, 1, 20)
    13.4
    >>> difr(1600, 1725, 0, 20)
    -6.6
    >>> difr(2000, 0, 1, 20)
    0.0
    """
    if elo2 == 0:
        return 0.0
    else:
        dif = elo1 - elo2
        if abs(dif) >= 400:
            dif = 400 * (abs(dif) / dif)
        if dif >= 0:
            for i in range(rows):
                if table_pd[i][0] <= dif <= table_pd[i + 1][0]:
                    dr = k * (result - table_pd[i + 1][1])
                    return dr
        elif dif < 0:
            for i in range(rows):
                if table_pd[i][0] <= abs(dif) <= table_pd[i + 1][0]:
                    dr = k * (result - 1 + table_pd[i + 1][1])
                    return dr


def difr(elo1: int, elo2: int, result: float, k: int) -> float:
    """(int,int,float,int) -> float
    Return rating difference base on 2 players ratings, result and development coefficient.

    >>> difr(1500, 1500, 0.5, 20)
    0.0
    >>> difr(1600, 1725, 1, 20)
    13.4
    >>> difr(1600, 1725, 0, 20)
    -6.6
    >>> difr(2000, 0, 1, 20)
    0.0
    """
    if elo2 == 0:
        return 0.0
    else:
        dif = elo1 - elo2
        if dif >= 0:
            for i in range(rows):
                if table_pd[i][0] <= dif <= table_pd[i + 1][0]:
                    dr = k * (result - table_pd[i + 1][1])
                    return dr
        elif dif < 0:
            for i in range(rows):
                if table_pd[i][0] <= abs(dif) <= table_pd[i + 1][0]:
                    dr = k * (result - 1 + table_pd[i + 1][1])
                    return dr


def total_elo_calculator(elo1: int, elo_opponents_results: list, k):
    elo_opponents_results.sort()
    beneficial_opponent = elo_opponents_results.pop(0)
    beneficial_elo = difr400(elo1, beneficial_opponent[0], beneficial_opponent[1], k)
    elo_list = [difr(elo1, elo_opponents_results[gyros][0], elo_opponents_results[gyros][1], k) for gyros in range(len(elo_opponents_results))]
    total_elo_difference = beneficial_elo + sum(elo_list)
    return total_elo_difference, (elo1+sum(elo_list))
