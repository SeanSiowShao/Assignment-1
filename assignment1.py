"""
Replace the contents of this module docstring with your own details.
"""


def main():
    print("Welcome to Sean Siow")
    print("Songs To Learn 1.0 - by <Your Name>")
    run_again = True
    while run_again:
        print("Menu:")
        print("L - List songs")
        print("A - Add new song")
        print("C - Complete a song")
        print("Q - Quit")
        file = open("songs.csv", mode="r+")
        ch = str(input(""))
        ch = ch.upper()
        if ch == "Q":
            print("Goodbye")
            run_again = False

        elif ch == "L":
            import csv
            num = 0

            with open("songs.csv") as f:
                file = csv.reader(f)
                for row in file:
                    num += 1
                    print(str(num) + " - ".join(row))

        elif ch == "C":
            li = []
            with open("songs.csv", "r") as file:
                for lines in file:
                    li.append(lines)
                print(li)
            print("please enter the number of song you want to complete")
            comp = int(input(""))
            new_str = ""
            for i in range(len(li)):
                if comp == (i + 1):
                    tmp_str = li[i]
                    tmp_str1 = tmp_str[:-2] + "n\n"
                    li[i] = tmp_str1
                    new_str = new_str + tmp_str1
                else:
                    new_str = new_str + li[i]
            with open("songs.csv", "w") as file2:
                file2.write(new_str)

        elif ch == "A":
            import csv
            with open('songs.csv', 'a') as file:
                file.write(str(
                    "{0} {1} {2} n\n".format(input("Please enter the titles"), str(input("please enter artist")),
                                             str(input("please enter year")))))


if __name__ == '__main__':
    main()
