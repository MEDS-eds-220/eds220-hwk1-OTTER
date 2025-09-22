OK_FORMAT = True

test = {   'name': 'q9',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> assert set(filtered_data.columns) >= {'PH', 'Salinity_mean', 'Depth'}, 'Missing required columns'\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> assert filtered_data.shape[1] == 3\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
