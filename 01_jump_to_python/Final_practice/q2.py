a = {'A': 90, 'B': 80}
try:
    print(a['C'])
except KeyError:
    print(70)