nums = int(input('Digite o valor da tabuada que queira: '))

for i in range(1, 11):
    tabuada = nums * i
    print('{} x {} = {}'.format(nums, i, tabuada))