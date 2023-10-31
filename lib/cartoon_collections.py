def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    captain_planet_calls = [call.capitalize() + '!' for call in planeteer_calls]
    return captain_planet_calls

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(items):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheese_types:
            return item
    return None
