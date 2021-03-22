import math

reward = 15

utilites = [0, 0, 0, reward]
disc = 0.2
delta = 0.01

a_right = [[0.8, 1, -1], [0.2, 0, -1]]
a_up = [[0.8, 2, -1], [0.2, 0, -1]]
b_left = [[0.8, 0, -1], [0.2, 1, -1]]
b_up = [[0.8, 3, -4], [0.2, 1, -1]]
c_right = [[0.25, 3, -3], [0.75, 2, -1]]
c_down = [[0.8, 0, -1], [0.2, 2, -1]]

iterat = 1

while True:

    print("Iteration number:", iterat)
    iterat += 1

    a_right_val = 0
    a_up_val = 0
    b_left_val = 0
    b_up_val = 0
    c_right_val = 0
    c_down_val = 0

    print("\n\nState A")
    print("action = right")
    print("Ur = ", end="")
    for arr in a_right:
        prob = arr[0]
        dest = arr[1]
        cost = arr[2]
        print("%f*(%f + 0.2*%f)"%(prob, cost, utilites[dest]), end=" + ")
        a_right_val += prob * (cost + disc * utilites[dest])
    print("\n=", a_right_val)

    print("\naction = up")
    print("Uu = ", end="")
    for arr in a_up:
        prob = arr[0]
        dest = arr[1]
        cost = arr[2]
        print("%f*(%f + 0.2*%f)"%(prob, cost, utilites[dest]), end=" + ")
        a_up_val += prob * (cost + disc * utilites[dest])
    print("\n=", a_up_val)

    print("\n\nState B")
    print("\naction = left")
    print("Ul = ", end="")
    for arr in b_left:
        prob = arr[0]
        dest = arr[1]
        cost = arr[2]
        print("%f*(%f + 0.2*%f)"%(prob, cost, utilites[dest]), end=" + ")
        b_left_val += prob * (cost + disc * utilites[dest])
    print("\n=", b_left_val)

    print("\naction = up")
    print("Uu = ", end="")
    for arr in b_up:
        prob = arr[0]
        dest = arr[1]
        cost = arr[2]
        print("%f*(%f + 0.2*%f)"%(prob, cost, utilites[dest]), end=" + ")
        b_up_val += prob * (cost + disc * utilites[dest])
    print("\n=", b_up_val)


    print("\n\nState C")
    print("\naction = right")
    print("Ur = ", end="")
    for arr in c_right:
        prob = arr[0]
        dest = arr[1]
        cost = arr[2]
        print("%f*(%f + 0.2*%f)"%(prob, cost, utilites[dest]), end=" + ")
        c_right_val += prob * (cost + disc * utilites[dest])
    print("\n=", c_right_val)

    print("\naction = down")
    print("Ud = ", end="")
    for arr in c_down:
        prob = arr[0]
        dest = arr[1]
        cost = arr[2]
        print("%f*(%f + 0.2*%f)"%(prob, cost, utilites[dest]), end=" + ")
        c_down_val += prob * (cost + disc * utilites[dest])
    print("\n=", c_down_val)

    new_util = []
    new_util.append(max(a_right_val, a_up_val))
    new_util.append(max(b_left_val, b_up_val))
    new_util.append(max(c_right_val, c_down_val))
    new_util.append(reward)

    print("A\n")
    print("Right: " + str(a_right_val))
    print("Up: " + str(a_up_val))
    print("Max: " + str(new_util[0]))
    print()

    print("B\n")
    print("Left: " + str(b_left_val))
    print("Up: " + str(b_up_val))
    print("Max: " + str(new_util[1]))
    print()

    print("C\n")
    print("Right: " + str(c_right_val))
    print("Down: " + str(c_down_val))
    print("Max: " + str(new_util[2]))
    print()

    bellman_error = -100
    for i in range(3):
        bellman_error = max(bellman_error, abs(new_util[i] - utilites[i]))

    print("Bellman Error: " + str(bellman_error))
    print()
    utilites = new_util
    if(bellman_error < delta):
        break

print("Last iteration\n")
a_right_val = 0
a_up_val = 0
b_left_val = 0
b_up_val = 0
c_right_val = 0
c_down_val = 0

for arr in a_right:
    prob = arr[0]
    dest = arr[1]
    cost = arr[2]
    a_right_val += prob * (cost + disc * utilites[dest])

for arr in a_up:
    prob = arr[0]
    dest = arr[1]
    cost = arr[2]
    a_up_val += prob * (cost + disc * utilites[dest])

for arr in b_left:
    prob = arr[0]
    dest = arr[1]
    cost = arr[2]
    b_left_val += prob * (cost + disc * utilites[dest])

for arr in b_up:
    prob = arr[0]
    dest = arr[1]
    cost = arr[2]
    b_up_val += prob * (cost + disc * utilites[dest])

for arr in c_right:
    prob = arr[0]
    dest = arr[1]
    cost = arr[2]
    c_right_val += prob * (cost + disc * utilites[dest])

for arr in c_down:
    prob = arr[0]
    dest = arr[1]
    cost = arr[2]
    c_down_val += prob * (cost + disc * utilites[dest])

new_util = []
new_util.append(max(a_right_val, a_up_val))
new_util.append(max(b_left_val, b_up_val))
new_util.append(max(c_right_val, c_down_val))
new_util.append(reward)

print("A\n")
print("Right: " + str(a_right_val))
print("Up: " + str(a_up_val))
print("Max: " + str(new_util[0]))
print()

print("B\n")
print("Left: " + str(b_left_val))
print("Up: " + str(b_up_val))
print("Max: " + str(new_util[1]))
print()

print("C\n")
print("Right: " + str(c_right_val))
print("Down: " + str(c_down_val))
print("Max: " + str(new_util[2]))
print()

bellman_error = -100
for i in range(3):
    bellman_error = max(bellman_error, abs(new_util[i] - utilites[i]))

print("Bellman Error: " + str(bellman_error))
print()
