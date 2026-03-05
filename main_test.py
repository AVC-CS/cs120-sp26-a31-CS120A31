import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # Input: 10 Class A, 20 Class B, 15 Class C
    # A=150.00, B=240.00, C=135.00, Total=525.00
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([
        r'150\.00',
        r'240\.00',
        r'135\.00',
        r'525\.00',
    ], lines)


@pytest.mark.T2
def test_main_2():
    # Input: 1 Class A, 2 Class B, 3 Class C
    # A=15.00, B=24.00, C=27.00, Total=66.00
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([
        r'15\.00',
        r'24\.00',
        r'27\.00',
        r'66\.00',
    ], lines)


@pytest.mark.T3
def test_main_3():
    # Input: 5 Class A, 5 Class B, 5 Class C
    # A=75.00, B=60.00, C=45.00, Total=180.00
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([
        r'75\.00',
        r'60\.00',
        r'45\.00',
        r'180\.00',
    ], lines)


@pytest.mark.T4
def test_main_4():
    # Input: 100 Class A, 50 Class B, 25 Class C
    # A=1500.00, B=600.00, C=225.00, Total=2325.00
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([
        r'1500\.00',
        r'600\.00',
        r'225\.00',
        r'2325\.00',
    ], lines)
