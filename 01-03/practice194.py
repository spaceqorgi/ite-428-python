premier_league_2017_2018 = [
    {"Pos":1,"Team":"Manchester City (C)","W":32,"D":4,"L":2,"GF":106,"GA":27},
    {"Pos":2,"Team":"Manchester United","W":25,"D":6,"L":7,"GF":68,"GA":28},
    {"Pos":3,"Team":"Tottenham Hotspur","W":23,"D":8,"L":7,"GF":74,"GA":36},
    {"Pos":4,"Team":"Liverpool","W":21,"D":12,"L":5,"GF":84,"GA":38},
    {"Pos":5,"Team":"Chelsea","W":21,"D":7, "L":10,"GF":62,"GA":38},
    {"Pos":6,"Team":"Arsenal","W":19,"D":6,"L":13,"GF":74,"GA":51},
    {"Pos":7,"Team":"Burnley","W":14,"D":12,"L":12,"GF":36,"GA":39},
    {"Pos":8,"Team":"Everton","W":13,"D":10,"L":15,"GF":44,"GA":58},
    {"Pos":9,"Team":"Leicester City","W":12,"D":11,"L":15,"GF":56,"GA":60},
    {"Pos":10,"Team":"Newcastle United","W":12,"D":8,"L":18,"GF":39,"GA":47},
    {"Pos":11,"Team":"Crystal Palace","W":11,"D":11,"L":16,"GF":45,"GA":55},
    {"Pos":12,"Team":"Bournemouth","W":11,"D":11,"L":16,"GF":45,"GA":61},
    {"Pos":13,"Team":"West Ham United","W":10,"D":12,"L":16,"GF":48,"GA":68},
    {"Pos":14,"Team":"Watford","W":11,"D":8,"L":19,"GF":44,"GA":64},
    {"Pos":15,"Team":"Brighton & Hove Albion","W":9,"D":13,"L":16,"GF":34,"GA":54},
    {"Pos":16,"Team":"Huddersfield Town","W":9,"D":10,"L":19,"GF":28,"GA":58},
    {"Pos":17,"Team":"Southampton","W":7,"D":15,"L":16,"GF":37,"GA":56},
    {"Pos":18,"Team":"Swansea City (R)","W":8,"D":9,"L":21,"GF":28,"GA":56},
    {"Pos":19,"Team":"Stoke City (R)","W":7,"D":12,"L":19,"GF":35,"GA":68},
    {"Pos":20,"Team":"West Bromwich Albion (R)","W":6,"D":13,"L":19,"GF":31,"GA":56}
]

def stat_point_goalD(data):
    for d in data:
        print('{:<4} {:<40} Pts: {:<6} GD: {:<6}'.format(
            d['Pos'],
            d['Team'].lower(),
            (d['W'] * 3) + d['D'],
            d['GF'] - d['GA']
        ))


def stat_percentages(data):
    for i, d in enumerate(data):
        n = float(d['W'] + d['L'] + d['D'])
        t = d['Team'].upper()
        w = d['W']/n*100
        dr = d['D']/n*100
        l = d['L']/n*100
        print('{:<4} {:<40} Win[{:.2f}%] Lose[{:.2f}%] Draw[{:.2f}%]'.format(
            i+1,
            t,
            w,
            dr,
            l
            ))

def sort_by_key(data):
    # Using lambda function to sort by "Team"
    return sorted(data, key=lambda k: k["Team"])

stat_point_goalD(premier_league_2017_2018)
print("")
stat_percentages(sort_by_key(premier_league_2017_2018))
