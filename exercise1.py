# start

pizzas: int = int(input("number total pieces of pizza:"))

friends = pizzas // 4

# There are one pizza
pieces_for_friends = pizzas // 4
total_pieces=pieces_for_friends % friends // 4
pizzas_left = pizzas % friends

print(f"Each friend received pieces:{pieces_for_friends},total_pieces:{total_pieces}")


# end
