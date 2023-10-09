from datetime import datetime


def main():
    with open("log.txt", "a") as file:
        file.write(f"Script executed at: {datetime.now()}\n")


if __name__ == "__main__":
    main()
