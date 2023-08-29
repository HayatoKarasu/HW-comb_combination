from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) Главное отличие размещений от сочетаний', fontsize=14)
plt.text(0.01, 0.8, 'в том что в размещении очень важен порядок,', fontsize=14)
plt.text(0.01, 0.7, 'а в сочетании порядок не имеет значения.', fontsize=14)
plt.text(0.01, 0.6, '2) У нас 7 космонавтов полетят 3-е.', fontsize=14)
plt.text(0.01, 0.5, 'Сколько способов отобрать?', fontsize=14)
form = r"$С_3^7 = \frac{7!}{3!(7-3)!} = \frac{7*6*5*4!}{3!*4!} = \frac{7*6*5}{3*2} = \frac{210}{6} = 35$"
plt.text(0.01, 0.4, form, fontsize=15)
plt.text(0.01, 0.3, '3) У нас 5 космонавтов: часть иследовать,', fontsize=14)
plt.text(0.01, 0.2, 'часть останется. Сколько комбинаций?', fontsize=14)
form = r"$C̄_4^5 = \frac{(5+4-1)!}{4!(5-1)!} = \frac{8!}{4!*4!} = \frac{8*7*6*5*4!}{4!*4*3*2} = \frac{1680}{24} = 70$"
plt.text(0.01, 0.1, form, fontsize=15)
plt.text(0.01, 0.01, '4-ка потому что 1 пойдет или останется', fontsize=14)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()