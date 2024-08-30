"""
https://docs.python.org/pt-br/3/library/stdtypes.html
imutáveis que vimos: str, int, float, bool
"""
string = 'Álvaro'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
#string[3] = 'ABC' - se a gnt tentar fazer isso vai dar errado pq esse tipo éum tipo imutável
#mas como eu faço pra aparecer isso, não faz, pq não da
print(string[3])
print(outra_variavel) #essa foi um jeito de fzr aquilo do comentário acima, mas não faz isso não, pq não da e é muito ruim
print(string.capitalize()) #esse método vai transformar a primeira letra em maiúscula
print(string.zfill(10)) #vai preencher com 0 a esquerda da string que será printada, no caso ali com 10 caracteres
#só que a string q vc printar estará inclusa nesses 10 caracteres