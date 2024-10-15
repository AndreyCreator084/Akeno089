def custom_write(file_name, strings):
    file = open(file_name, "w+", encoding="utf-8")
    strings_positions = {}
    for string in range(0, len(strings)):
        file.read()
        byte_strings = file.tell()
        file.write(f'{strings[string]}\n')
        strings_positions[(string + 1, byte_strings)] = strings[string]
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)