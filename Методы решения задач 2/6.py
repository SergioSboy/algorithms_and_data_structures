def sort_down(type_of_coins):
    for i in range(m - 1):
        id_of_max = i
        for j in range(i + 1, m):
            if type_of_coins[j] > type_of_coins[id_of_max]:
                id_of_max = j
        type_of_coins[i], type_of_coins[id_of_max] = type_of_coins[id_of_max], type_of_coins[i]


def select(type_of_coins, selected_coins, final_row, size, num_in_type, cur_sum, end_in_sel):
    global is_n, is_more_than_n, is_less_than_n
    if cur_sum == n:
        if end_in_sel < size:
            size = end_in_sel
            final_row[:size + 1] = selected_coins[:size + 1]
        is_n = True
        return
    if num_in_type == m or cur_sum > n:
        if cur_sum > n:
            is_more_than_n = True
        return
    if cur_sum != 0 and cur_sum < n:
        is_less_than_n = True
    for i in range(2, -1, -1):
        cur_sum += type_of_coins[num_in_type] * i
        for j in range(1, i + 1):
            end_in_sel += 1
            selected_coins[end_in_sel] = type_of_coins[num_in_type]
        num_in_type += 1
        select(type_of_coins, selected_coins, final_row, size, num_in_type, cur_sum, end_in_sel)
        num_in_type -= 1
        cur_sum -= type_of_coins[num_in_type] * i
        end_in_sel -= i



is_n = False
is_more_than_n = False
is_less_than_n = False

n, m = map(int, input().split())
type_of_coins = list(map(int, input().split()))

sort_down(type_of_coins)

selected_coins = [0] * (m * 2)
final_row = [0] * (m * 2)
num_in_type = 0
end_in_sel = -1
cur_sum = 0
size = m * 2

select(type_of_coins, selected_coins, final_row, size, num_in_type, cur_sum, end_in_sel)

if is_n:
    print(size)
    print(*final_row[:size])
elif is_more_than_n:
    print(0)
else:
    print(-1)
