import collections

x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

cx = collections.Counter(x_list)
cy = collections.Counter(y_list)

print(cx.most_common()[1][0], cy.most_common()[1][0])
