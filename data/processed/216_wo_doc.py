import pandas as pd
import os
import json
from collections import Counter


def task_func(json_dir_path, word_count):
    """ 
    Analyze text content in JSON files from a given directory and find the most common words.
    
    This function reads all the JSON files in the specified directory, extracts the text content from each file,
    and determines the most frequent words. It then returns a list of the specified number of the most common words 
    and their respective counts.
    
    Parameters:
    json_dir_path (str): The directory path where JSON files are stored.
    word_count (int): The number of most common words to return.

    Returns:
    list: A list of tuples with the most common words and their counts.

    Requirements:
    - pandas
    - os
    - json
    - collections.Counter

    Example:
    >>> import tempfile
    >>> fake_data_1 = {"text": "Top visit morning price certainly indicate time. Figure add cold behind customer also."}
    >>> fake_data_2 = {"text": "Itself to current listen. Cover add will feeling head. Perform family affect reduce political general."}
    >>> temp_dir = tempfile.TemporaryDirectory()
    >>> with open(f"{temp_dir.name}/fake_data_1.json", 'w') as f:
    ...     json.dump(fake_data_1, f)
    >>> with open(f"{temp_dir.name}/fake_data_2.json", 'w') as f:
    ...     json.dump(fake_data_2, f)
    >>> task_func(temp_dir.name, 2)
    [('add', 2), ('Top', 1)]
    """

    word_counter = Counter()
    for filename in os.listdir(json_dir_path):
        if filename.endswith('.json'):
            with open(os.path.join(json_dir_path, filename), 'r') as f:
                data = json.load(f)
                text = data.get('text', '')
                words = pd.Series(text.split())
                word_counter += Counter(words)
    return word_counter.most_common(word_count)

import unittest
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create temporary JSON files for testing using tempfile
        fake_data_1 = {
            "text": "Top visit morning price certainly indicate time. Figure add cold behind customer also." 
            "Much join industry rate matter. Grow whether blue piece performance. And spend design speak "
            "available evening. Network choice under wear. Listen world ago life hard list bag. Recently office "
            "become network total student which color. Then director decision activity through new. Likely "
            "scientist up. While little position statement. Other worker key local least."
        }
        fake_data_2 = {
            "text": "Itself to current listen. Cover add will feeling head. Perform family affect reduce "
            "political general. Goal thought their treatment five born. In near his look recently treat. Read "
            "know her drug without determine. Want surface president whatever staff. Adult soon second together "
            "his wind. Early north voice magazine most enough pattern. Government hear back discussion admit "
            "measure pick. Market final former defense. Effort leg many reflect. Responsibility phone national "
            "beat none. Community current condition season ball sure administration final."
        }
        fake_data_3 = {
            "text": "Public plant program few close firm peace. Audience imagine attorney agreement team turn. "
            "Necessary put character. People research plan agent read its. Seem impact door represent final. See "
            "magazine pretty short next church. Bring last even wrong. Possible its impact join year. My final "
            "use road. Box tough training participant network remember. Baby trouble natural nation boy there "
            "yourself. Miss daughter address run with. Pull work bar lose."
        }
        fake_data_4 = {
            "text": "Live federal whatever single official deep. Effect TV store go should amount us threat. Admit "
            "science law family everyone now. Soldier southern group that response attack personal. Carry water "
            "list military capital activity. Trade say father manage Democrat. Their big upon green practice feeling. "
            "Policy five dark represent across stand dark most. Woman western certain success condition community "
            "appear. Event subject whose success economy."
        }
        fake_data_5 = {
            "text": "Security board interview ready there without fire. Street write somebody officer front he "
            "agency. Heart later year TV garden. Support able peace thousand push success skin. Peace eight eight "
            "between. Officer cup necessary reveal. End court skill book ground law finish world. Worry east author "
            "chance report military per. Build share entire might beautiful brother. Maintain great edge more "
            "family full market."
        }
        fake_data_6 = {
            "text": "Son sing teach finish window face community. Mean lawyer world good. Back political tax "
            "structure control or difficult last. Current nice just whatever interesting. Share ago information "
            "price never. Administration yes along north simply seem sister. Various instead record school effort "
            "medical. Arm happen generation perform those special realize. Meet admit seek reduce. Ground begin "
            "price keep modern especially statement. Argue key if use. Beautiful matter it concern quickly do. "
            "Win avoid away blue someone. There authority behind camera station."
        }
        fake_data_7 = {
            "text": "You ground seek. Collection fall action security. Very stage growth act develop. Cell hope "
            "clearly begin. Begin almost section contain read him. Across many smile drop perhaps system. Not push "
            "her kind song fight much. Southern boy hear other democratic. Home especially really around fall "
            "computer evidence. Bag decide father old area change. Research final manage day mind prove tend. "
            "Institution group involve mother set we. Season national issue level president."
        }
        fake_data_8 = {
            "text": "Official court point sit. Good stay return. Hard attorney son nice compare. Collection fly dog "
            "term. When wall program manage each street modern value. Reflect area travel every Republican miss "
            "research. Treatment line difficult feeling another professional hospital. Apply good person opportunity "
            "learn subject hotel. Cultural subject tell seven he use team. Together through run common relationship "
            "just. Box human interest expert student less area. Job become senior ahead himself."
        }
        fake_data_9 = {
            "text": "Place so per approach. Difference low business. Card institution course will defense develop. "
            "Growth usually great note above knowledge myself. Enough focus serve few until because ready. Ground "
            "stuff region high. Region probably large program. Continue true Mr success school."
        }
        fake_data_10 = {
            "text": "Plan buy candidate. Pay factor all whole heart Republican prove rise. Family state maybe watch. "
            "Sport improve worry care knowledge perhaps company thus. Away sport shake rich article pay born. Bag "
            "source how white. Several purpose year short six. Economic practice form bill. Top face thank girl "
            "together phone on him. Answer myself cultural suddenly attention. Answer understand great effect "
            "evidence state pick. Painting make time she stock."
        }
        # Create a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        # Write fake data to JSON files in the temporary directory
        for i, fake_data in enumerate([fake_data_1, fake_data_2, fake_data_3, fake_data_4, fake_data_5, fake_data_6,
                                       fake_data_7, fake_data_8, fake_data_9, fake_data_10], 1):
            with open(f"{self.temp_dir.name}/fake_data_{i}.json", 'w') as f:
                json.dump(fake_data, f)
    def tearDown(self):
        # Delete temporary directory
        self.temp_dir.cleanup()
    def test_case_1(self):
        # Testing with 3 most common words
        result = task_func(f"{self.temp_dir.name}/", 3)
        # Expecting 'Hello' to be the most common word based on our mock data
        self.assertEqual(result[0][0], 'success')
        self.assertEqual(len(result), 3)
    def test_case_2(self):
        # Testing with 5 most common words
        result = task_func(f"{self.temp_dir.name}/", 5)
        self.assertEqual(len(result), 5)
    def test_case_3(self):
        # Testing with all words
        result = task_func(f"{self.temp_dir.name}/", 100)
        self.assertTrue('world.' not in [word[0] for word in result])
    def test_case_4(self):
        # Testing with non-existent directory
        with self.assertRaises(FileNotFoundError):
            task_func('./non_existent_dir/', 3)
    def test_case_5(self):
        # Testing with 0 most common words (should return an empty list)
        result = task_func(f"{self.temp_dir.name}/", 0)
        self.assertEqual(result, [])
