
from rhombus.models.ek import EK

def setup(dbsession):
    assert dbsession

    EK.bulk_insert( ek_initlist, dbsession=dbsession)

ek_initlist = [
    (   '@SPECIES', None,
        [   ('Pf', 'P falciparum'),
            ('Pf/Pv', 'Mixed Pf / Pv'),
            ('Pv', 'P vivax')
        ]),

    (   '@BLOOD-WITHDRAWAL', 'Blood widthdrawal method',
        [   ('NA', 'Not available'),
            'venous',
            'capillary',
        ]),
    (   '@BLOOD-STORAGE', 'Blood storage/source method',
        [   ('NA', 'Not available'),
            'EDTA',
            'blood tube',
            'filter paper',
        ]),
    (   '@PCR-METHOD', 'PCR identification method',
        [   ('NA', 'Not available'),
        ]),
    (   '@EXTFIELD', None,
        [   'severity',
        ]),
    ]
