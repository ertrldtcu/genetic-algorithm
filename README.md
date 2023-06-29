# Genetik Algoritma

Bu kod deposunda Akıllı Sistemler dersi için hazırladığım Genetik Algoritma projemin kaynak kodları bulunmaktadır.

## GeneticAlgorithm Sınıfı

Verilen bir bit dizisinin tersinin bulunması problemi için çözüm üretilmiştir.

### Kurulum

Sadece `random` kütüphanesi içe aktarılmıştır. Eğer kullanılacaksa grafik çizimleri için `matplotlib.pyplot` gerekmektedir.

### Parametreler
#### GeneticAlgorithm(population_size, crossover_rate, mutation_rate, source_gene, iteration_count=-1, target_fitness=1):
- `population_size` (int): Her nesilde kullanılacak olan popülasyonun birey sayısı.
- `crossover_rate` (float): Yeni oluşturulan çocukların çaprazlamaya uğrama oranı [0.0 - 1.0].
- `mutation_rate` (float): Yeni oluşturulan çocukların mutasyona uğrama oranı [0.0 - 1.0].
- `source_gene` (array): Kaynak aynı zamanda hedef yani elde edilmesi istenen gen.
- `iteration_count` (int): Oluşturulacak maksimum nesil sayısı. `-1` olması durumunda istenen gen bulunana kadar devam eder.
- `target_fitness` (float): İstenen minimum başarı oranı. `1` olması durumunda istenen gen bulunana kadar devam eder [0.0 - 1.0].

## Örnek

[genetic algorithm.ipynb](genetic%20algorithm.ipynb) not defteri içerisinde yukarıda belirtilen problem için örnek bulunmaktadır. Kaynak kodu kendi probleminize göre düzenledikten sonra yine bu not defterini kullanabilirsiniz.
