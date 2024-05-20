def get_pack_used(pack_name):

    if len(pack_name) == 26:
        return "Laddering Pack"
    elif len(pack_name) == 24:
        return "Classic Pack"
    else:
        return "Unknown Pack"
def get_pack_factory(pack_name):
    import os
    if os.path.exists(f"./packs/packfac.csv"):
        packfac=[]
        with open(f"./packs/packfac.csv", "r") as f:
            for line in f:
                packfac.append(line.strip().split(","))

    if len(pack_name) == 26 or len(pack_name) == 24:
        packfaccod=pack_name[0:2]
        for i in packfac:
            if i[0]==packfaccod:
                return i[1]
        return "Unknown Factory"
    else:
        return "Unknown Factory"

