import collections

def most_frequent_item_count(collection):
    if (len(collection) == 0):
        return 0
    counter = collections.Counter(collection)
    return max(counter.values())
