def act(board):
    row = int(board.split(" ")[0])  # 행
    col = int(board.split(" ")[1])  # 열
    block_n = 0

    bomb = []
    blocks = []

    for i in range(row):
        temp = input()
        block_n += len(list(temp)) - list(temp).count("*") - list(temp).count(".")
        blocks.append(list(temp))

    print(block_n)
    print(block.index("A"))
    while block_n != 0:             # 블록이 없을때까지 반복
        for i in range(65,91):         # A부터 Z까지 순서대로
            for r in range(row):            # 첫째줄부터
                for l in range(col):            # 첫째칸부터
                    if blocks[r][l] == chr(i):      # 알파벳

                    

print(act(input()))