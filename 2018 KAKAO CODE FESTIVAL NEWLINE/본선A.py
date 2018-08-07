n = int(input())

first_1 = 5000000
second_1 = 3000000
third_1 = 2000000
forth_1 = 500000
fifth_1 = 300000
sixth_1 = 100000

first_2 = 5120000
second_2 = 2560000
third_2 = 1280000
forth_2 = 640000
fifth_2 = 320000

m_prize = 0

for i in range(n):
    a, b = input().split()

    if int(a) > 0:
        if int(a) == 1:
            m_prize = first_1
        elif int(a) <= 3:
            m_prize = second_1
        elif int(a) <= 6:
            m_prize = third_1
        elif int(a) <= 10:
            m_prize = forth_1
        elif int(a) <= 15:
            m_prize = fifth_1
        elif int(a) <= 21:
            m_prize = sixth_1

    if int(b) > 0:
        if int(b) == 1:
            m_prize += first_2
        elif int(b) <= 3:
            m_prize += second_2
        elif int(b) <= 7:
            m_prize += third_2
        elif int(b) <= 15:
            m_prize += forth_2
        elif int(b) <= 31:
            m_prize += fifth_2

    print(m_prize)
    m_prize = 0
