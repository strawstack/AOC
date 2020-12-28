image = [int(x) for x in list(open("input.txt").read()[:-1])]

layers = []
width  = 25
height = 6
index = 0
for _ in range(len(image)//(25 * 6)):
    # Each layer
    layer = []
    for h in range(height):
        row = []
        for w in range(width):
            row.append(image[index])
            index += 1
        layer.append(row)
    layers.append(layer)

def sol():
    bindex = 0
    bvalue = float("inf")
    for i in range(len(layers)):
        layer = layers[i]
        count = 0
        for row in layer:
            count += row.count(0)
        if count < bvalue:
            bvalue = count
            bindex = i
    ones, twos = 0, 0
    for row in layers[bindex]:
        ones += row.count(1)
        twos += row.count(2)
    return ones * twos

ans = sol()
print(ans)
