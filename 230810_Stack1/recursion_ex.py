selected = [0, 0, 0]


# idx 번째 요소에 idx+1 넣어주기
def put_number(idx):
    if idx != len(selected):
        selected[idx] = idx + 1
        return put_number(idx + 1)



result = put_number(0)
put_number(0)

print(selected)
print(result)