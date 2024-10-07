import handlers as h


def main():
    lines = [(10, 10, 90, 90), (120, 120, 130, 130), (50, 50, 150, 150), (-10, -10, 110, 110)]

    list(map(lambda line: print(h.cohen_sutherland(*line)), lines))


if __name__ == '__main__':
    main()
