"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
         {
        "input": [
            ('Alice', 'Bob'),
            ('Alice', 'Carol'),
            ('Bob', 'Alice'),
            ('Bob', 'Dave'),
            ('Carol', 'Alice'),
            ('Carol', 'Eve'),
            ('Dave', 'Bob'),
            ('Eve', 'Carol')
        ],
        "answer": {
            "Alice": ["Bob", "Carol"],
            "Bob": ["Alice", "Dave"],
            "Carol": ["Alice", "Eve"],
            "Dave": ["Bob"],
            "Eve": ["Carol"]
        }
    },
    {
        "input": [
            ('Alice', 'Bob'),
            ('Carol', 'Frank'),
            ('Bob', 'Carol'),
            ('Frank', 'Carol')
        ],
        "answer": {
            "Alice": ["Bob"],
            "Carol": ["Frank"],
            "Bob": ["Carol"],
            "Frank": ["Carol"]
        }
    }
    ]
}
