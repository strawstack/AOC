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

    final = []
    for _ in range(6):
        final.append([0 for x in range(25)])
    for layer in reversed(layers):
        for r in range(6):
            for c in range(25):
                if layer[r][c] == 0:
                    final[r][c] = "\u2B1B"

                elif layer[r][c] == 1:
                    final[r][c] = "\u2B1C"

    for r in range(6):
        for c in range(25):
            print(final[r][c], end="")
        print("")

ans = sol()
print(ans)
