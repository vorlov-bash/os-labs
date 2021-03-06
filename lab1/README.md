# ==Lab 1==

## Імітація алокатора на мові програмування python3
Алокатор несе у собі користь, через ефективність розприділення пам'яті між різними програмами, та має спеціальні алгоритми для цього.

Звичайний примітивний алокатор складається з хідерів та блоків: хідер містить у собі інформацію про виділений блок, а блок використовується вже самою програмою.
* Хідер складається з 3 байтів `(0, 0, 0)`
  * 1 байт використовується для перевірки вільності блока. Якщо блок вільний, то байт буде дорівнювати 0, в іншому випадку - 1.
  * 2 байт містить у собі інформацію про розмір попереднього блоку. Це зроблено для зручнішого і ефективнішого об'єндання пустих блоків, так як складність алгоритму складає `O(1)`
  * 2 байт містить у собі інформацію про розмір блоку, який відповідає нашому хідеру. Також зроблено для ефективності.
* Блок складається з n байтів `(0, ..., 0)`

Код алокатора повністю задокументований, та перевірений.

## Використання
Щоб змінити код алокатора, потрібно зайти у директорію `lab1` і відкрити файл `__init__.py`. У цьому файлі вже є приклад використання, але за бажанням, його можна модифікувати.

Щоб запустити приклад достатньо перейти у головну папку та ввести команду:
```
python3 manage.py --lab 1
```
