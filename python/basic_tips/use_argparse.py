import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Convert schedule.yaml to ical.')
    parser.add_argument('-r', '--read', type=argparse.FileType('r'),
                        help='YAML file explains the schedule.')

    return parser.parse_args()


if __name__ == '__main__':
    print(main())
