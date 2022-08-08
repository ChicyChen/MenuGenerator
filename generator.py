import random
import argparse

def read_menu(filename):

    txt_file = open(filename, "r")
    file_content = txt_file.read()
    # print("The file content are: ", file_content)

    content_list = file_content.split("\n")
    txt_file.close()
    # print("The list is: ", content_list)

    return content_list

def select_menu(content_list, num):
    random.shuffle(content_list)
    if (num > len(content_list)):
        num = len(content_list)
    result = []
    for i in range(num):
        result.append(content_list[i])
    return result


def main():
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('-n', '--num', dest="num", type=int, default='5',
                        help='number of menu')
    parser.add_argument('-m', '--menu', dest="menu", type=str, default="dinner_menu.txt",
                        help='type of menu')

    args = parser.parse_args()

    filename = args.menu
    num = args.num
    
    content_list = read_menu(filename)
    result = select_menu(content_list, num)
    print(result)
    

if __name__ == "__main__":
    main()