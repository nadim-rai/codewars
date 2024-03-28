'''
We are diligently pursuing our elusive operative, Matthew Knight, who also goes by the alias Roy Miller. 
He employs a nomadic lifestyle to evade detection, constantly moving from one location to another, with 
each of his journeys following a perplexing and non-standard sequence of itineraries. Our mission is to 
decipher the routes he will undertake during each of his voyages.

Task
You've been provided with an array of itinerary routes, decipher the precise destinations he will visit
in the correct sequence according to his meticulously planned itineraries.

Example
Based on the provided routes:
[ [USA, BRA], [JPN, PHL], [BRA, UAE], [UAE, JPN] ]

The correct sequence of destinations is:

"USA, BRA, UAE, JPN, PHL"
'''

routes_ = [('BRA','KSA'), ('USA','BRA'), ('JPN','PHL'), ('KSA','UAE'), ('UAE','JPN')]

def find_routes(routes):
    
    trace = []
    for currentPair in routes:
        if not any(point[1] == currentPair[0] for point in routes):
            trace.append(currentPair[0])
            trace.append(currentPair[1])
    for _ in range(len(routes)):
        for currentPair in routes:
            if currentPair[0] == trace[-1]:
                trace.append(currentPair[1])
    return ', '.join(trace)

print(find_routes(routes_))      #'USA, BRA, KSA, UAE, JPN, PHL'

# def find_routes(routes: list) -> str:
#     d = dict(routes)
#     res = list(d.keys() - d.values())
#     while res[-1] in d: res.append(d[res[-1]])
#     return ', '.join(res)

# solved by chivery, FizzyLearner59, reem_elouzi
