"""
Декартово произведение
"""

colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']

out = [(i, j) for i in colors for j in sizes]
print(out)
