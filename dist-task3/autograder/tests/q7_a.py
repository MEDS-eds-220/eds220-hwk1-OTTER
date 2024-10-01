OK_FORMAT = True

test = {   'name': 'q7_a',
    'points': 1,
    'suites': [   {   'cases': [{'code': ">>> assert pd.read_csv('data/t3_q7a_df.csv', index_col = 0).equals(pd.DataFrame(top20))\n", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
