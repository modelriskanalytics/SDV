import pandas as pd

DEMO_METADATA = {
    'tables': [
        {
            'name': 'users',
            'primary_key': 'user_id',
            'fields': [
                {
                    'name': 'user_id',
                    'type': 'id',
                },
                {
                    'name': 'country',
                    'type': 'categorical',
                },
                {
                    'name': 'gender',
                    'type': 'categorical',
                },
                {
                    'name': 'age',
                    'type': 'numerical',
                    'subtype': 'integer'
                }
            ]
        },
        {
            'name': 'sessions',
            'primary_key': 'session_id',
            'fields': [
                {
                    'name': 'session_id',
                    'type': 'id',
                },
                {
                    'name': 'user_id',
                    'ref': {
                        'field': 'user_id',
                        'table': 'users'
                    },
                    'type': 'id',
                },
                {
                    'name': 'device',
                    'type': 'categorical',
                },
                {
                    'name': 'os',
                    'type': 'categorical',
                }
            ]
        },
        {
            'name': 'transactions',
            'primary_key': 'transaction_id',
            'fields': [
                {
                    'name': 'transaction_id',
                    'type': 'id',
                },
                {
                    'name': 'session_id',
                    'ref': {
                        'field': 'session_id',
                        'table': 'sessions'
                    },
                    'type': 'id',
                },
                {
                    'name': 'timestamp',
                    'type': 'datetime',
                    'format': '%Y-%m-%d'
                },
                {
                    'name': 'amount',
                    'type': 'numerical',
                    'subtype': 'float'
                },
                {
                    'name': 'approved',
                    'type': 'boolean'
                }
            ]
        }
    ]
}


def load_demo():
    """Load demo data.

    The demo data consists of the metadata and tables dict for a a toy dataset with
    three simple tables:

        * users: user data including country, gender and age.
        * sessions: sessions data with a foreign key to user.
        * transactions: transactions data with a foreign key to sessions.

    Returns:
        tuple:
            metadata and tables dict.
    """
    users = pd.DataFrame({
        'user_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'country': ['USA', 'UK', 'ES', 'UK', 'USA', 'DE', 'BG', 'ES', 'FR', 'UK'],
        'gender': ['M', 'F', None, 'M', 'F', 'M', 'F', None, 'F', None],
        'age': [34, 23, 44, 22, 54, 57, 45, 41, 23, 30]
    })
    sessions = pd.DataFrame({
        'session_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'user_id': [0, 1, 1, 2, 4, 5, 6, 6, 6, 8],
        'device': ['mobile', 'tablet', 'tablet', 'mobile', 'mobile',
                   'mobile', 'mobile', 'tablet', 'mobile', 'tablet'],
        'os': ['android', 'ios', 'android', 'android', 'ios',
               'android', 'ios', 'ios', 'ios', 'ios']
    })
    transactions = pd.DataFrame({
        'transaction_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'session_id': [0, 0, 1, 3, 5, 5, 7, 8, 9, 9],
        'timestamp': ['2019-01-01T12:34:32', '2019-01-01T12:42:21', '2019-01-07T17:23:11',
                      '2019-01-10T11:08:57', '2019-01-10T21:54:08', '2019-01-11T11:21:20',
                      '2019-01-22T14:44:10', '2019-01-23T10:14:09', '2019-01-27T16:09:17',
                      '2019-01-29T12:10:48'],
        'amount': [100.0, 55.3, 79.5, 112.1, 110.0, 76.3, 89.5, 132.1, 68.0, 99.9],
        'approved': [True, True, True, False, False, True, True, False, True, True],
    })
    transactions['timestamp'] = pd.to_datetime(transactions['timestamp'])

    tables = {
        'users': users,
        'sessions': sessions,
        'transactions': transactions
    }

    return DEMO_METADATA.copy(), tables