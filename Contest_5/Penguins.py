def draw_penguin():
    penguin = [
        "   _~_    ",
        "  (o o)   ",
        " /  V  \  ",
        "/(  _  )\ ",
        "  ^^ ^^   "
    ]
    return penguin


def print_penguins(num_penguins):
    penguin_lines = draw_penguin()

    for line in penguin_lines:
        print(line * num_penguins)


def main():
    n = int(input())
    print_penguins(n)


if __name__ == "__main__":
    main()
