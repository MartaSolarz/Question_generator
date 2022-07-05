# Generator pytań przygotowawczych do egzaminu - 2.07.2022

import csv
from dataclasses import dataclass
import random
import sys
import time

FILENAME = 'pytania.csv'

@dataclass
class Quest:
    question: str
    answer: str

    def __post_init__(self):
        if not self.question:
            raise ValueError('Blank question field')
        elif not self.answer:
            raise ValueError('Blank answer field')


def csv_reader() -> list[Quest]:
    with open(FILENAME, encoding='utf8') as stream:
        elements = csv.DictReader(stream)
        question_bank = create_question_bank(elements)

    return question_bank


def escape_error() -> None:
    print()
    ask = input('-- if you want to interrupt and correct the contents of the file: use back -- ')
    if ask == 'back':
        sys.exit(1)


def create_question_bank(elements:dict[str,str]) -> list[Quest]:
    question_bank = []
    for el in elements:
        try:
            quest = Quest(el['PYTANIE'], el['ODP'])
        except ValueError as v:
            print(f'ERROR: {v.args[0]}')
            escape_error()
        else:
            question_bank.append(quest)
    
    return question_bank


def generate_random_question(questions:list[Quest]) -> Quest:
    random_question = random.choice(questions)  

    return random_question 


def show_answer(random_question:Quest) -> None:
    ask_for_answer = input('Pokazać odpowiedź? [t/n] ') 

    if ask_for_answer.lower() == 't':
        print('Odpowiedź:', random_question.answer)
        print()


def repeat(random_question:Quest, generated_yet:list[Quest]) -> list[Quest]:
    ask_for_repetitive = input('Czy dodać to pytanie ponownie do puli? [t/n] ')

    if not ask_for_repetitive.lower() == 't':
        generated_yet.append(random_question)
    else:
        print('Dodano.')

    return generated_yet


def main():
    question_bank = csv_reader()
    generated_yet = []

    print()
    print('GENERATOR PYTAŃ - jeśli chcesz zakończyć użyj funkcji exit')
    
    while True:
        print()
        ask = input('-- click enter to generate new question or use exit -- ')

        if ask == 'exit':
            break
        
        while True:
            random_question = generate_random_question(question_bank)

            if not random_question in generated_yet:
                print('Wylosowane pytanie: ', random_question.question)
                print()

                time.sleep(10)

                show_answer(random_question)
                generated_yet = repeat(random_question, generated_yet)

                break

            elif len(question_bank) == len(generated_yet):
                print()
                print('Gratulacje, to już wszystkie pytania!')
                sys.exit(2)
    
    print()
    print(f'Liczba przerobionych pytań: {len(generated_yet)} z {len(question_bank)}.' )


if __name__ == '__main__':
    main()