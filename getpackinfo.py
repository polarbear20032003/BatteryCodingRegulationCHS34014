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

        f.close()
    else:
        return "Unknown Factory"

    if len(pack_name) == 26 or len(pack_name) == 24:
        packfaccod=pack_name[0:2]
        for i in packfac:
            if i[0]==packfaccod:
                return i[1]
        return "Unknown Factory"
    else:
        return "Unknown Factory"

def get_pack_type(pack_name):
    if len(pack_name) == 26 or len(pack_name) == 24:
        if pack_name[3] == "P":
            return "动力蓄电池包"
        elif pack_name[3] == "M":
            return "蓄电池模块"

        elif pack_name[3] == "C":
            return "单体蓄电池"
        else:
            return "未知类型"
