
from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    C_plusplus = ProgrammingLanguage("C++", "Static", False, 1983)
    java = ProgrammingLanguage("Java", "Static", True, 1995)

    languages = [ruby, python, visual_basic, C_plusplus, java]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()