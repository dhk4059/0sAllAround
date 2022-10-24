import sys

from testcode import testcode
from testoutputs import testoutputs
from interpreterv1 import Interpreter

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    num_passed = 0

    start = 0
    end = len(testcode)
    # end = 1
    for i in range(start, end):
        print(f'TEST {i + 1}:')
        for j in range(100):
            print('=', end='')
        print()
        print('OUTPUT (if any):')
        program_code = testcode[i].splitlines()

        # run that shit
        test1 = Interpreter(console_output=False)
        try:
            test1.run(program_code)
            actual = "\n".join(test1.get_output())
            print(actual)
        except Exception as e:
            err = f'{test1.error_type} {test1.error_line}'
            actual = "\n".join(test1.get_output()) + \
                f'\n{err}' if len(test1.get_output()) > 0 else err
            print(actual)
            print(e)

        print()
        print('EXPECTED OUTPUT:')
        expected = testoutputs[i]
        print(expected)
        print()
        print()
        if actual == expected:
            print("PASS")
            num_passed += 1
        else:
            print("FAIL")
        for j in range(100):
            print('=', end='')
        print()
        print()
        print()

    print(f"{num_passed}/{end}")
