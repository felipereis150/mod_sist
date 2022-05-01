# creating csv file to Distribuição de Frequência
import csv

header = ['Sexo', 'Idade', 'Carreira Pretendida', 'N Irmaos', 'Discipl. Fav', 'Renda em Sal. Min']
data = [
    ['Masculino',16,'Humanas',2,'História',11,2],
    ['Masculino',17,'Biológicas',3,'Biologia',18,5],
    ['Feminino',15,'Humanas',2,'Geografia',12,1],
    ['Masculino',14,'Exatas',1,'Matemática',11,5],
    ['Feminino',14,'Exatas',1,'Geografia',10],
    ['Feminino',15,'Biológicas',0,'Química',10,7],
    ['Masculino',15,'Biológicas',0,'Biológica',11,6],
    ['Masculino',15,'Exatas',1,'Português',12,4],
    ['Masculino',19,'Humanas',3,'Português',15,9],
    ['Feminino',15,'Biológicas',1,'Química',9,6],
    ['Feminino',20,'Humanas',4,'História',16,3],
    ['Masulino',17,'Humanas',0,'Matemática',12,9],
    ['Masculino',16,'Humanas',1,'História',13,4],
    ['Feminino',16,'Humanas',2,'Geografia',13,2],
    ['Feminino',16,'Biológicas',2,'Matemática',11,7],
    ['Feminino',18,'Humanas',2,'Geografia',17,6],
    ['Masculino',15,'Exatas',1,'Matemática',12,6],
    ['Masculino',18,'Exatas',3,'Física',13,1],
    ['Masculino',18,'Biológicas',4,'Química',15,4],
    ['Masculino',14,'Biológicas',1,'Física',8,7],
]

# with open('distribuicao_de_freq.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)

with open('distribuicao_de_freq.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)