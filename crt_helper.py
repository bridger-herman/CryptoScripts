import sys

def main():
    if len(sys.argv) < 5:
        print('bad argument')
        print('crt_helper.py a m b n [total_num]')
        print('a mod m, b mod n')
        return
    if len(sys.argv) == 6:
        total_num = int(sys.argv[5])
    else:
        total_num = 10
    a, m, b, n = [int(n) for n in sys.argv[1:5]]
    first = [a + m*i for i in range(total_num)]
    last = [b + n*i for i in range(total_num)]
    for i in range(total_num):
        for j in range(total_num):
            if first[i] == last[j]:
                print('num:', first[i])
                print('  {}%{} = {}'.format(first[i], m, first[i]%m))
                print('  {}%{} = {}'.format(first[i], n, first[i]%n))
                print('  {}%{} = {}'.format(first[i], n*m, first[i]%(n*m)))
                print()


if __name__ == '__main__':
    main()
