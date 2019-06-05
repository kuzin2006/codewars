attributes = {}

try:
    var = attributes['zone_name']
except KeyError:
    var = "undefined"
finally:
    print(var)