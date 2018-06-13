from pyramid.config import Configurator
from rhombus.lib.utils import cerr, cout, set_dbhandler_class
from rhombus import add_route_view

#from plasmogen_snp.models.handler import DBHandler
import plasmogen_snp.scripts.run
#set_dbhandler_class( DBHandler )

from genaf_snp import includeme as genaf_snp_includeme, init_app
from genaf_snp.views.tools import set_form_factory

from plasmogen_snp.views.tools import plasmogen_snp_form_factory



def includeme( config ):


    # specific plasmogen_snp configuration

    add_route_view( config, 'plasmogen_snp.views.subject', 'plasmogen_snp.subject',
        '/subject',
        '/subject/@@action',
        '/subject/{id}@@edit',
        '/subject/{id}@@save',
        ('/subject/{id}', 'view')

    )

    # set essential pages
    config.add_route('home', '/')
    config.add_view('plasmogen_snp.views.home.index', route_name = 'home')

    config.add_route('login', '/login')
    config.add_view('plasmogen_snp.views.home.login', route_name = 'login')

    config.add_route('logout', '/logout')
    config.add_view('plasmogen_snp.views.home.logout', route_name = 'logout')

    add_route_view( config, 'plasmogen_snp.views.docs', 'plasmogen_snp.docs',
        #'/docs{path:.*}@@view',
        #'/docs{path:.*}@@edit',
        #'/docs{path:.*}@@save',
        #'/docs{path:.*}@@action',
        ('/docs{path:.*}', 'index'),
    )

    # set other related functions

    import genaf_snp.views.sample, plasmogen_snp.views.sample
    genaf_snp.views.sample.set_format_sampleinfo( plasmogen_snp.views.sample.format_sampleinfo )

    # include genaf_snp configuration
    config.include( genaf_snp_includeme)

    config.add_view('plasmogen_snp.views.tools.sample.index', route_name='tools-sample')

    config.override_asset('rhombus:templates/base.mako', 'plasmogen_snp:templates/base.mako')
    config.override_asset('rhombus:templates/plainbase.mako', 'plasmogen_snp:templates/plainbase.mako')


    return config



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    cerr('plasmogen_snp main() in running...')
    config = init_app(global_config, settings, prefix='/mgr')
    config.include(includeme)

    cover_template = settings.get('override.cover', None)
    if cover_template:
        config.override_asset( 'plasmogen_snp:templates/cover.mako', cover_template)

    set_form_factory(plasmogen_snp_form_factory)

    return config.make_wsgi_app()
