import sys

if __name__ == '__main__':
    text = ' '.join(sys.argv[1:])

    hello = (
        '________',
        f'< {text} >',
        '--------',
        ' \\',
        '  \\',
        '     /\_)o<',
        '    |      \\',
        '    | O . O|',
        '     \_____/'
    )

    print('\n'.join(hello))
