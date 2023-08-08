def start_spring(**exam_obj):
    result = ''
    spring_obj = {}
    for key, value in exam_obj.items():
        if value not in spring_obj:
            spring_obj[value] = []
        spring_obj[value].append(key)
        
    sorted_coll_obj = sorted(spring_obj.items(), key=lambda x: (-len(x[1]), x[0]))
    for coll_obj in sorted_coll_obj:
        type_obj = coll_obj[0]
        list_obj = coll_obj[1]
        sorted_list_of_objects = sorted(list_obj)
        result += f"{type_obj}:\n"
        for obj in sorted_list_of_objects:
            result += f"-{obj}\n"
    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
