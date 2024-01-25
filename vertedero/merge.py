# merge.py
def merge(dict1, dict2):
    res = dict1.copy()   # make a copy of dict1
    res.update(dict2)    # modify the copy with dict2's keys and values
    return res
