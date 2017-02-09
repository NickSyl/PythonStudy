import logging


def fool(s):
    return 100 / int(s)


def main():
    try:
        fool('aa')
    except Exception as e:
        logging.exception(e)

main()
print("end")
