import json
from CharmCord.globeHandler import get_globals


async def getGlobalUserVar(args, context):
    all_vars = get_globals()[2]

    ag = args.split(";")
    user = ag[0].replace("<@", "").replace(">", "")
    var = ag[1]
    try:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
            return total[f"{user}_{var}"]
    except KeyError:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
        with open("variables.json", "w") as variables:
            total.update({f"{user}_{var}": all_vars[var]})
            json.dump(total, variables)
            return all_vars[var]
