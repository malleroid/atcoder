sx, xy, tx, ty = map(int, input().split())

ans = ""

ans += "U"*(ty-xy)
ans += "R"*(tx-sx)
ans += "D"*(ty-xy)
ans += "L"*(tx-sx+1)
ans += "U"*(ty-xy+1)
ans += "R"*(tx-sx+1)
ans += "DR"
ans += "D"*(ty-xy+1)
ans += "L"*(tx-sx+1)
ans += "U"

print(ans)
