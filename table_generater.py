def generate_table(num):
    for i in range(1,11):
        print(f"{num} X {i}= {num * i}")

num = int(input('Enter the number:'))
generate_table(num)