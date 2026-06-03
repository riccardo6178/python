import sys

def main():
    print(f'Numero totale di argomenti:{len(sys.argv)}\n')
    print(f'nome del programma:{sys.argv[0]}\n')
    print(f'Arogmento 1:{sys.argv[1]}\n')
    print(f'Tutti gli argomenti:{sys.argv[0:]}')

if __name__=="__main__":
    main()