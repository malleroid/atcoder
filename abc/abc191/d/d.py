X, Y, R = map(float, input().split())

ans = 0
i = X-R
j = Y-R

while X-R <= i <= X+R:

    while Y-R <= j <= Y+R:

        if (i-X)**2+(j-Y)**2 <= R**2:
            ans += 1

        j += 1

    i += 1

print(ans)
