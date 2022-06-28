# open api database 추출
# https://opentdb.com/api_config.php
# https://opentdb.com/api.php?amount=50&type=boolean
import html_theory

import requests

parameters = {
    'amount' : 50,
    'type' : "boolean",
}

#response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
#print(question_data)

#data 중 알수없는 글자 변환 : html character entities : entity name or entity number
#&quot; --- "
#&#39 --- '
#freeformatter.com
#python 함수 : html.unescape(데이터)
#각가의 데이터에 적용

'''
{'response_code': 0,
 'results': [{'category': 'Animals', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The Axolotl is an amphibian that can spend its whole life in a larval state.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The common software-programming acronym &quot;I18N&quot; comes from the term &quot;Interlocalization&quot;.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The first computer bug was formed by faulty wires.', 'correct_answer': 'False',
              'incorrect_answers': ['True']}, 
              {'category': 'General Knowledge', 'type': 'boolean', 'difficulty': 'easy',
               'question': 'The Great Wall of China is visible from the moon.',
               'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Entertainment: Film', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The movie &quot;The Nightmare before Christmas&quot; was all done with physical objects.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Music', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Soulja Boy&#039;s &#039;Crank That&#039; won a Grammy for Best Rap Song in 2007.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Geography', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Vatican City is a country.', 'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'History', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The Spitfire originated from a racing plane.', 'correct_answer': 'True',
              'incorrect_answers': ['False']},
             {'category': 'Science & Nature', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Steel is an alloy of Iron and Carbon.', 'correct_answer': 'True',
              'incorrect_answers': ['False']}, {'category': 'Animals', 'type': 'boolean', 'difficulty': 'easy',
                                                'question': 'Kangaroos keep food in their pouches next to their children.',
                                                'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Geography', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'History', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Brezhnev was the 5th leader of the USSR.', 'correct_answer': 'True',
              'incorrect_answers': ['False']},
             {'category': 'Entertainment: Japanese Anime & Manga', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'In Kill La Kill, the weapon of the main protagonist is a katana. ',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'General Knowledge', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Bulls are attracted to the color red.', 'correct_answer': 'False',
              'incorrect_answers': ['True']}, {'category': 'Science & Nature', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Salt is 100% composed of Sodium.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Politics', 'type': 'boolean', 'difficulty': 'easy', 'question': 'Denmark has a monarch.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Mythology', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'According to Norse mythology, Loki is a mother.', 'correct_answer': 'True',
              'incorrect_answers': ['False']},
             {'category': 'General Knowledge', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The Sun rises from the North.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Solid Snake is actually a clone from the DNA of Big Boss in the Metal Gear Solid series&#039; history.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Politics', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Russia passed a law in 2013 which outlaws telling children that homosexuals exist.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The PlayStation was originally a joint project between Sega and Sony that was a Sega Genesis with a disc drive.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Vehicles', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'When BMW was established in 1916, it was producing automobiles.', 'correct_answer': 'False',
              'incorrect_answers': ['True']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The Sniper&#039;s SMG in Team Fortress 2, was originally intended to be the Scout&#039;s primary weapon.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'TF2: The Medic will be credited for an assist if he heals a Spy that successfully saps a building.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The main playable character of the 2015 RPG &quot;Undertale&quot; is a monster.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Geography', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'St. Louis is the capital of the US State Missouri.', 'correct_answer': 'False',
              'incorrect_answers': ['True']},
             {'category': 'Entertainment: Board Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'There is a Donald Trump Board Game, which was made in 1989.', 'correct_answer': 'True',
              'incorrect_answers': ['False']}, {'category': 'History', 'type': 'boolean', 'difficulty': 'medium',
                                                'question': 'Abraham Lincoln was the first U.S. President to be born outside the borders of the thirteen original states. ',
                                                'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Science: Computers', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Music', 'type': 'boolean', 'difficulty': 'medium',
              'question': '&quot;The Division Bell&quot; is the final album of the progressive rock band Pink Floyd.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Entertainment: Music', 'type': 'boolean', 'difficulty': 'hard',
              'question': 'The band STRFKR was also briefly known as Pyramiddd.', 'correct_answer': 'True',
              'incorrect_answers': ['False']},
             {'category': 'Entertainment: Board Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': '&quot;PAYDAY: The Heist&quot; is a sequel to the board game &quot;Payday&quot;.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Sports', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'In association football, or soccer, a corner kick is when the game restarts after someone scores a goal.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'In Riot Games &quot;League of Legends&quot; the name of Halloween event is called &quot;The Reckoning&quot;.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'Entertainment: Japanese Anime & Manga', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'In &quot;JoJo&#039;s Bizarre Adventure&quot;, Father Enrico Pucchi uses a total of 3 stands in Part 6: Stone Ocean.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Art', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Leonardo da Vinci was not the creator of the Mona Lisa.', 'correct_answer': 'False',
              'incorrect_answers': ['True']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'The game &quot;Pocket Morty&quot; has a Morty called &quot;Pocket Mortys Morty&quot;?',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'easy',
              'question': 'Several characters in &quot;Super Mario 64&quot; blink their eyes, including Mario himself.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Hidden in the files for &quot;Mario Kart Arcade GP&quot; is a picture of the Beslan school hostage crisis.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Science & Nature', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Pneumonoultramicroscopicsilicovolcanoconiosis is a synonym for the disease known as silicosis.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Geography', 'type': 'boolean', 'difficulty': 'hard',
              'question': 'The two largest ethnic groups of Belgium are Flemish and Walloon. ',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Video Games', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The scrapped Sonic the Hedgehog 2 level &quot;Hidden Palace Zone&quot; was later reused in the iOS port of the game. ',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Animals', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Tigers have one colour of skin despite the stripey fur.', 'correct_answer': 'False',
              'incorrect_answers': ['True']}, {'category': 'Geography', 'type': 'boolean', 'difficulty': 'easy',
                                               'question': 'Rhode Island is actually located on the US mainland, despite its name.',
                                               'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'Entertainment: Music', 'type': 'boolean', 'difficulty': 'hard',
              'question': 'The singer Billie Holiday was also known as &quot;Lady Day&quot;.', 'correct_answer': 'True',
              'incorrect_answers': ['False']}, {'category': 'History', 'type': 'boolean', 'difficulty': 'medium',
                                                'question': 'The Korean War ended in 1953 without any ceasefire.',
                                                'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'General Knowledge', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The British organisation CAMRA stands for The Campaign for Real Ale.',
              'correct_answer': 'True', 'incorrect_answers': ['False']},
             {'category': 'General Knowledge', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.',
              'correct_answer': 'False', 'incorrect_answers': ['True']},
             {'category': 'History', 'type': 'boolean', 'difficulty': 'medium',
              'question': 'Franz Joseph I was the last emperor of Austria.', 'correct_answer': 'False',
              'incorrect_answers': ['True']}]}
'''
'''
question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The first computer bug was formed by faulty wires.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    }
]
'''
