# coding: utf-8

# 兄弟姉妹(けいていしまい)翻訳組み合わせ
# Sibling translation combination

## 実運用向けに記載した方
SIBLINGS_KANJI: str = '兄弟姉妹'

def main(input: str):
    SIBLINGS_HIRAGANA: str = 'きょうだい'
    SIBLINGS_PAIR: dict = {
        '兄弟': 'きょうだい',
        '姉妹': 'しまい',
        '兄姉': 'けいし',
        '兄妹': 'けいまい',
        '姉弟': 'してい',
        '弟妹': 'ていまい'}

    if (input in SIBLINGS_PAIR):
        output: str = SIBLINGS_HIRAGANA
        if (SIBLINGS_PAIR[input] != SIBLINGS_HIRAGANA):
            output += f'(or {SIBLINGS_PAIR[input]})'
        return print(output)

    return print(f'{SIBLINGS_KANJI}じゃないよ')

if __name__ == "__main__":
    input: str = input(f'{SIBLINGS_KANJI}のペアを入力して下さい -> ')
    main(input.replace(' ', ''))

# イメージしやすいようにコーディングした方
# input = input('兄弟姉妹のペアを入力して下さい -> ')
# if ('兄弟' == input):
#     print('きょうだい')
# elif ('姉妹' == input):
#     print('きょうだい(or しまい)')
# elif ('兄姉' == input):
#     print('きょうだい(or けいし)')
# elif ('兄妹' == input):
#     print('きょうだい(or けいまい)')
# elif ('姉弟' == input):
#     print('きょうだい(or してい)')
# elif ('弟妹' == input):
#     print('きょうだい(or ていまい)')
# else:
#     print('兄弟姉妹じゃないよ')
