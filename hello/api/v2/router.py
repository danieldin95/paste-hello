import pecan
import controllers.root as root


def v2_factory(global_config, **local_config):
    print 'v2_factory:', 'global_conf =', global_config, 'kwargs =', local_config
    app = pecan.make_app(root.RootController(),
                         debug=False,
                         force_canonical=False,
                         guess_content_type_from_ext=True)
    return app


def APIRouter(**local_config):
    return v2_factory(None, **local_config)


def _factory(global_config, **local_config):
    return v2_factory(global_config, **local_config)


setattr(APIRouter, 'factory', _factory)
