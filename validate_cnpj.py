import modules_cnpj

CNPJs = [
    '04.252.011/0001-10',
    '04.252.011/0001-11',
    '40.688.134/0001-61',
    '40.688.134/0001-63',
    '71.506.168/0001-11',
    '12.544.992/0001-05',
    '00.000.000/0000-00',
    '123',
    '89.709.498/0001-70',
    '76.935.616/0001-16',
    '35.453.436/0001-11'
]

for cnpj in CNPJs:
    valid = modules_cnpj.check_cnpj(cnpj)
    print(f'CNPJ No. {cnpj} is {"valid." if valid else "not valid."}')

print()

for i in range(10):
    new_cnpj = modules_cnpj.new_cnpj_generator()
    formatted = modules_cnpj.format_cnpj(new_cnpj)
    print(f'New CNPJ No. {formatted}')