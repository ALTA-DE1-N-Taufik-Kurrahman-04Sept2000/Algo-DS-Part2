def count_item_and_sort(items):
    item_count = {}
    
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    sorted_items = sorted(item_count.items(), key=lambda x: (x[1], x[0]))
    
    result = ""
    for item, count in sorted_items:
        result += f"{item}->{count} "
    
    return result.strip()

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"