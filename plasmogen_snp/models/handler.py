
from genaf_snp.models.handler import DBHandler as genaf_DBHandler
from plasmogen_snp.models.sample import PlasmogenSample, Batch, Subject

from rhombus.lib.utils import cerr


class DBHandler(genaf_DBHandler):

    Sample = PlasmogenSample
    Batch = Batch
    Subject = Subject


    def initdb(self, create_table=True, init_data=True, rootpasswd=None):
        super().initdb(create_table, init_data, rootpasswd=rootpasswd)
        if init_data:
            from plasmogen_snp.models.setup import setup
            setup( self.session() )
            cerr('[plasmogen] Database has been initialized.')


    def __repr__(self):
        return "<DBHandler from PlasmoGen>"


    def search_subject(self, code, auto=False):
        return self.Subject.search( code, 'U', 0, auto, dbsession = self.session() )


DBHandler.set_sample_class( PlasmogenSample )





