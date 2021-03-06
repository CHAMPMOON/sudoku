class SudokuPrinter:
    @staticmethod
    def print(puzzle):
        print_sdk = list()
        for line in puzzle:
            print_sdk.extend(line)
        print('┏━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓'
              '\n┃  {0}  {1}  {2}  ┃  {3}  {4}  {5}  ┃  {6}  {7}  {8}  ┃'
              '\n┃  {9}  {10}  {11}  ┃  {12}  {13}  {14}  ┃  {15}  {16}  {17}  ┃'
              '\n┃  {18}  {19}  {20}  ┃  {21}  {22}  {23}  ┃  {24}  {25}  {26}  ┃'
              '\n┣━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫'
              '\n┃  {27}  {28}  {29}  ┃  {30}  {31}  {32}  ┃  {33}  {34}  {35}  ┃'
              '\n┃  {36}  {37}  {38}  ┃  {39}  {40}  {41}  ┃  {42}  {43}  {44}  ┃'
              '\n┃  {45}  {46}  {47}  ┃  {48}  {49}  {50}  ┃  {51}  {52}  {53}  ┃'
              '\n┣━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫'
              '\n┃  {54}  {55}  {56}  ┃  {57}  {58}  {59}  ┃  {60}  {61}  {62}  ┃'
              '\n┃  {63}  {64}  {65}  ┃  {66}  {67}  {68}  ┃  {69}  {70}  {71}  ┃'
              '\n┃  {72}  {73}  {74}  ┃  {75}  {76}  {77}  ┃  {78}  {79}  {80}  ┃'
              '\n┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┛'.format(*print_sdk))