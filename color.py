import random
def get_color():
    colors = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan"]
    index = random.randint(0,len(colors)-1)
    return colors[index]
