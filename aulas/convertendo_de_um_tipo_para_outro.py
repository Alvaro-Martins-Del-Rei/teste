#conversão de tipos, coerção
#type convertion, typecasting, coercion
#é o ato de converter um tipo em outro
#tipos imutáveis e primitivos: str, int, float e bool
print('1', type('1'))
print(int('1'), type(int('1'))) #mostrando como trasnformar um str em int e mostrando o tipo
print(int('1') + 1) #mostrando como transformar str em int e somando a outro int
print(type(float('1') + 1)) #somando o tipo float a um int = float, e mostrando o seu tipo tudo de uma vez
print(bool('')) #uma str sem valor é considerada False
print(bool(' ')) #uma str com valor, até mesmo um espaço, é considerada True
print(str(11) + 'b') #transformando um int em str e concatenando com outra str