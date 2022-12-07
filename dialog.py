"""
Człowiek pyta, robot odpowiada

    Człowiek: Cześć Robot, jak się nazywasz?
    Robot: Nazywam się Nexiobot. A Tobie jak na imię?
    Cz: Adam
    R: Adam, zadaj mi jakieś pytanie.
    Cz: Która jest godzina?   # allready impolemented
    R: <godzina>. Czy poranna kawa już była?
    Cz: Nie. A u Ciebie?
    R: Ja wolę napięcie płynące z prądu.
    Cz: Robot, czy wiesz, jak się nazywał robot z Gwiezdnych wojen?
    R: R2-D2
    Cz: Czy oglądasz Mundial?
    R: Zerkam jednym okiem i widzę sporo niespodzianek.
    Cz: Rozmawiasz przez telefon?
    R: Tak, bardzo często. To mój kontakt ze światem. Na Black Week kupiłem nowy telefon.
    Cz: Zimno na dworze. Jakie plany na wieczór?
    R: Pojechałbym w nieznane, tam gdzie ciepło.

Robot pyta, człowiek odpowiada

    R: Jaki jest Twój ulubiony kolor?
    Cz: <kolor>
    R: <kolor z tabelki> to <znaczenie koloru z tabelki>.
    lub
    R: <kolor spoza listy> - większość mężczyzn nie zna takiego koloru i ja do nich należę.
"""


from typing import Optional, Dict, FrozenSet


__replics = {
        'Nazywam się Nexiobot. A Tobie jak na imię?': frozenset('jak na imię'.split()),
        'Nazywam się Nexiobot. A Tobie jak na imię?': frozenset('jak się nazywasz'.split()),
        # '': frozenset(),
        # '': frozenset(),
        # '': frozenset(),
        # '': frozenset(),
        # '': frozenset(),
        # '': frozenset(),
        }


class Dialog:

    __phrase: str
    __client_name: str
    __name_was_asked = False

    def __init__(self) -> None:
        while True:
            self.chat()

    def chat(self) -> None:
        self.__phrase: str = input('say some shit...')
        if self.__name_was_asked:
            self. __name_was_asked = False
            self.__client_name = self.__phrase.split()[0].capitalize()
            print(f'{self.__client_name}, zadaj mi jakieś pytanie.')
        self.__clear_phrase()
        answer = self.get_answer()
        if "jak na imię" in answer.lower():
            self. __name_was_asked = True
        print(answer)

    def __clear_phrase(self):
        self.__phrase = ''.join([_.lower() for _ in self.__phrase if _.isalpha() or _.isspace()])

    def get_answer(self) -> str:
        phrase = frozenset(self.__phrase.split())
        for answer, key_words in __replics.items():
            if key_words.issubset(phrase):
                return answer
        return ''
    

Dialog()
