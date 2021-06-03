def set_operations_with_dict():
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    d1 = dict(pairs)
    print("딕셔너리1\t: {0}".format(d1))

#set_operations_with_dict()

    d2 = {"a": 1, "c": 2, "d": 3, "e":4}
    intersection =  d1.keys() & d2.keys()
    print("{0}".format(intersection))

    intersection_items = d1.items() & d2.items()
    print(intersection_items)

    subtraction1 = d1.keys() - d2.keys()
    print(subtraction1)

    d3 ={key: d2[key] for key in d2.keys() - {"c", "d"}}
    print(d3)
set_operations_with_dict()