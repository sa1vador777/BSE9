#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

def main(count: int) -> [list[dict]]:
    list_stud: list[dict] = []
    list_smart_stud: list[dict] = []
    i = 0
    while i < count:
        print(f"Введите данные студента {i+1}")
        name = input("Введите ФИО: ")
        group = int(input("Введите группу: "))
        marks = list(map(int, list(input("Введите 5 оценок через пробел: ").split(' '))))
        list_stud.append(dict([["ФИО", name], ["Группа", group], ["Успеваемость", marks]]))
        i+=1
    for element in list_stud:
        if sum(element["Успеваемость"]) / len(element["Успеваемость"]) > 4.0:
            list_smart_stud.append(element)
    list_smart_stud=sorted(list_smart_stud, key=lambda x: x["Группа"])
    return list_smart_stud


if __name__ == "__main__":
    count = int(input("Введите кол-во учащихся: "))
    pprint(main(count))
