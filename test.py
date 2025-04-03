from calculate import square

def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError as e:
        print(f"Test failed: {e}")
    try:
        assert square(3) == 9
    except AssertionError as e:
        print(f"Test failed: {e}")
    try:
        assert square(4) == 16
    except AssertionError as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    main()