def usual_dict(dict_data):
    newdata = {}
    for k, v in dict_data:
        if k in newdata:
            newdata[k].append(v)
        else:
            newdata[k] = [v]
    return newdata

def setdefault_dict(dict_data):
    newdata = {}

    for k ,v in dict_data:
        newdata.setdefault(k, []).append(v)
    return newdata

def test_setdef():
    dic_data = (("key1", "value1"),
    ("key1", "value2"),
    ("key2", "value3"),
    ("key2", "value4"),("key2", "value5"))

    print(usual_dict(dic_data))
    print(setdefault_dict(dic_data))


test_setdef()