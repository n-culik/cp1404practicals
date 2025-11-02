"""
CP1404 Practical
Email name extraction
Date: 27.10.2025
Author: Nicola Culik
Estimate: 50 min
Actual:  26 min
"""
from programming_language import ProgrammingLanguage

languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
             ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
             ProgrammingLanguage("Visual Basic", "Static", False, 1991),
]

dynamic_languages = [language for language in languages if language.is_dynamic()]
print("The dynamically typed languages are:")
for language in dynamic_languages:
    print(language.name)