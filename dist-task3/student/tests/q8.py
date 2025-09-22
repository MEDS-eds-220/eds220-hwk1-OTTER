OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> assert pd.read_csv('data/t3_q8_df.csv', index_col=0).equals(top20_filtered)\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
