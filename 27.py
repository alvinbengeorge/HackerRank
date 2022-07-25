if __name__ == '__main__':
    s = input()
    print(
        any([_.isalnum() for _ in s]),
        any([_.isalpha() for _ in s]),
        any([_.isdigit() for _ in s]),
        any([_.islower() for _ in s]),
        any([_.isupper() for _ in s]),
        sep="\n"
    )