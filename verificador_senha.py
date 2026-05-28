print("Digite uma senha que contém:")
print("- 8 caracteres")
print("- números, letras maiúsculas, minúsculas e caracteres especiais")
senha = input("Senha: ")

tamanho = len(senha)
tem_maiusculas = any(c.isupper() for c in senha)
tem_minusculas = any(c.islower() for c in senha)
tem_digitos = any(c.isdigit() for c in senha)
tem_caracteres_especiais = any(not c.isalnum() for c in senha)

criterios = [
    tamanho >= 8,
    tem_maiusculas,
    tem_minusculas,
    tem_digitos,
    tem_caracteres_especiais
]

if criterios == [True, True, True, True, True]:
    print("Senha forte atende a todos os critérios de segurança")
elif criterios.count(True) >= 2 and criterios.count(True) < 5:
    print("Senha média pois atende a alguns critérios, mas não todos")
else:    
    print("Senha não atende aos critérios mínimos de segurança")