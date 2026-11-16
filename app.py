"""Greeting application for the Jenkins CI/CD lab."""


def greet(name):
    return f"Hello, {name} from Mohammad Kourani!"


def main():
    print(greet("World"))


if __name__ == "__main__":
    main()
