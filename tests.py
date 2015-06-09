import os
import shutil
import tempfile
import unittest

from scripttest import TestFileEnvironment


class BaseTemplateTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(
            os.path.join(self.tempdir, 'test-output'),
            ignore_hidden=False,
        )

    def create_template(self):
        """Run mr.bob to create your template."""
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
            'project': self.project,
        }
        return self.env.run(
            '%(dir)s/bin/mrbob -O %(project)s --config '
            '%(dir)s/test_answers_%(template)s.ini %(dir)s/bobtemplates/simplesconsultoria/%(template)s'
            % options)


class AddOnTemplateTest(BaseTemplateTest):
    """Tests for the `addon` template."""
    template = 'addon'
    project = 'customer.site.addon'

    def test_addon_template(self):
        """Test the `addon` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project + '/.travis.yml',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/CHANGES.rst',
                self.project + '/CONTRIBUTORS.rst',
                self.project + '/docs',
                self.project + '/docs/LICENSE.GPL',
                self.project + '/docs/LICENSE.txt',
                self.project + '/Makefile',
                self.project + '/MANIFEST.in',
                self.project + '/README.rst',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/customer',
                self.project + '/src/customer/__init__.py',
                self.project + '/src/customer/site',
                self.project + '/src/customer/site/__init__.py',
                self.project + '/src/customer/site/addon',
                self.project + '/src/customer/site/addon/__init__.py',
                self.project + '/src/customer/site/addon/config.py',
                self.project + '/src/customer/site/addon/configure.zcml',
                self.project + '/src/customer/site/addon/interfaces.py',
                self.project + '/src/customer/site/addon/profiles',
                self.project + '/src/customer/site/addon/profiles.zcml',
                self.project + '/src/customer/site/addon/profiles/default',
                self.project + '/src/customer/site/addon/profiles/default/browserlayer.xml',
                self.project + '/src/customer/site/addon/profiles/default/metadata.xml',
                self.project + '/src/customer/site/addon/profiles/uninstall',
                self.project + '/src/customer/site/addon/profiles/uninstall/customer.site.addon.txt',
                self.project + '/src/customer/site/addon/setuphandlers.py',
                self.project + '/src/customer/site/addon/testing.py',
                self.project + '/src/customer/site/addon/tests',
                self.project + '/src/customer/site/addon/tests/__init__.py',
                self.project + '/src/customer/site/addon/tests/test_example.robot',
                self.project + '/src/customer/site/addon/tests/test_robot.py',
                self.project + '/src/customer/site/addon/tests/test_setup.py',
                self.project + '/src/customer/site/addon/upgrades',
                self.project + '/src/customer/site/addon/upgrades/__init__.py',
                self.project + '/src/customer/site/addon/upgrades/configure.zcml',
                self.project + '/src/customer/site/addon/upgrades/v2',
                self.project + '/src/customer/site/addon/upgrades/v2/__init__.py',
                self.project + '/src/customer/site/addon/upgrades/v2/configure.zcml',
                self.project + '/src/customer/site/addon/upgrades/v2/profile',
                self.project + '/src/customer/site/addon/upgrades/v2/profile/metadata.xml',
                self.project,
            ]
        )


class ContentTypeTemplateTest(BaseTemplateTest):
    """Tests for the `contenttype` template."""
    template = 'contenttype'
    project = 'customer.site.contenttype'

    def test_addon_template(self):
        """Test the `contenttype` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project + '/.travis.yml',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/CHANGES.rst',
                self.project + '/CONTRIBUTORS.rst',
                self.project + '/docs',
                self.project + '/docs/LICENSE.GPL',
                self.project + '/docs/LICENSE.txt',
                self.project + '/Makefile',
                self.project + '/MANIFEST.in',
                self.project + '/README.rst',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/customer',
                self.project + '/src/customer/__init__.py',
                self.project + '/src/customer/site',
                self.project + '/src/customer/site/__init__.py',
                self.project + '/src/customer/site/contenttype',
                self.project + '/src/customer/site/contenttype/__init__.py',
                self.project + '/src/customer/site/contenttype/browser',
                self.project + '/src/customer/site/contenttype/browser/__init__.py',
                self.project + '/src/customer/site/contenttype/browser/configure.zcml',
                self.project + '/src/customer/site/contenttype/browser/templates',
                self.project + '/src/customer/site/contenttype/browser/templates/helloworld.pt',
                self.project + '/src/customer/site/contenttype/browser/view.py',
                self.project + '/src/customer/site/contenttype/config.py',
                self.project + '/src/customer/site/contenttype/configure.zcml',
                self.project + '/src/customer/site/contenttype/content',
                self.project + '/src/customer/site/contenttype/content/__init__.py',
                self.project + '/src/customer/site/contenttype/content/example.py',
                self.project + '/src/customer/site/contenttype/interfaces.py',
                self.project + '/src/customer/site/contenttype/profiles',
                self.project + '/src/customer/site/contenttype/profiles.zcml',
                self.project + '/src/customer/site/contenttype/profiles/default',
                self.project + '/src/customer/site/contenttype/profiles/default/browserlayer.xml',
                self.project + '/src/customer/site/contenttype/profiles/default/metadata.xml',
                self.project + '/src/customer/site/contenttype/profiles/default/rolemap.xml',
                self.project + '/src/customer/site/contenttype/profiles/default/types',
                self.project + '/src/customer/site/contenttype/profiles/default/types.xml',
                self.project + '/src/customer/site/contenttype/profiles/default/types/Example.xml',
                self.project + '/src/customer/site/contenttype/profiles/uninstall',
                self.project + '/src/customer/site/contenttype/profiles/uninstall/customer.site.contenttype.txt',
                self.project + '/src/customer/site/contenttype/static',
                self.project + '/src/customer/site/contenttype/static/document_icon.png',
                self.project + '/src/customer/site/contenttype/testing.py',
                self.project + '/src/customer/site/contenttype/tests',
                self.project + '/src/customer/site/contenttype/tests/__init__.py',
                self.project + '/src/customer/site/contenttype/tests/test_content.py',
                self.project + '/src/customer/site/contenttype/tests/test_example.robot',
                self.project + '/src/customer/site/contenttype/tests/test_robot.py',
                self.project + '/src/customer/site/contenttype/tests/test_setup.py',
                self.project + '/src/customer/site/contenttype/upgrades',
                self.project + '/src/customer/site/contenttype/upgrades/__init__.py',
                self.project + '/src/customer/site/contenttype/upgrades/configure.zcml',
                self.project + '/src/customer/site/contenttype/upgrades/v1010',
                self.project + '/src/customer/site/contenttype/upgrades/v1010/__init__.py',
                self.project + '/src/customer/site/contenttype/upgrades/v1010/configure.zcml',
                self.project + '/src/customer/site/contenttype/upgrades/v1010/handler.py',
                self.project + '/src/customer/site/contenttype/upgrades/v1010/profile',
                self.project + '/src/customer/site/contenttype/upgrades/v1010/profile/metadata.xml',
                self.project,
            ]
        )


class TemaTemplateTest(BaseTemplateTest):
    """Tests for the `theme` template."""
    template = 'theme'
    project = 'customer.site.theme'

    def test_tema_template(self):
        """Test the `theme` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project,
                self.project + '/.travis.yml',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/CHANGES.rst',
                self.project + '/CONTRIBUTORS.rst',
                self.project + '/docs',
                self.project + '/docs/LICENSE.GPL',
                self.project + '/docs/LICENSE.txt',
                self.project + '/Makefile',
                self.project + '/MANIFEST.in',
                self.project + '/README.rst',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/customer',
                self.project + '/src/customer/__init__.py',
                self.project + '/src/customer/site',
                self.project + '/src/customer/site/__init__.py',
                self.project + '/src/customer/site/theme',
                self.project + '/src/customer/site/theme/__init__.py',
                self.project + '/src/customer/site/theme/browser',
                self.project + '/src/customer/site/theme/browser/__init__.py',
                self.project + '/src/customer/site/theme/browser/configure.zcml',
                self.project + '/src/customer/site/theme/browser/viewlets',
                self.project + '/src/customer/site/theme/browser/viewlets/__init__.py',
                self.project + '/src/customer/site/theme/browser/viewlets/configure.zcml',
                self.project + '/src/customer/site/theme/browser/viewlets/path_bar.py',
                self.project + '/src/customer/site/theme/browser/viewlets/templates',
                self.project + '/src/customer/site/theme/browser/viewlets/templates/path_bar.pt',
                self.project + '/src/customer/site/theme/config.py',
                self.project + '/src/customer/site/theme/configure.zcml',
                self.project + '/src/customer/site/theme/Extensions',
                self.project + '/src/customer/site/theme/Extensions/__init__.py',
                self.project + '/src/customer/site/theme/Extensions/Install.py',
                self.project + '/src/customer/site/theme/interfaces.py',
                self.project + '/src/customer/site/theme/profiles',
                self.project + '/src/customer/site/theme/profiles.zcml',
                self.project + '/src/customer/site/theme/profiles/default',
                self.project + '/src/customer/site/theme/profiles/default/browserlayer.xml',
                self.project + '/src/customer/site/theme/profiles/default/cssregistry.xml',
                self.project + '/src/customer/site/theme/profiles/default/jsregistry.xml',
                self.project + '/src/customer/site/theme/profiles/default/metadata.xml',
                self.project + '/src/customer/site/theme/profiles/default/theme.xml',
                self.project + '/src/customer/site/theme/profiles/uninstall',
                self.project + '/src/customer/site/theme/profiles/uninstall/customer.site.theme.txt',
                self.project + '/src/customer/site/theme/profiles/uninstall/theme.xml',
                self.project + '/src/customer/site/theme/testing.py',
                self.project + '/src/customer/site/theme/tests',
                self.project + '/src/customer/site/theme/tests/__init__.py',
                self.project + '/src/customer/site/theme/tests/test_browserlayer.py',
                self.project + '/src/customer/site/theme/tests/test_setup.py',
                self.project + '/src/customer/site/theme/tests/test_theme.py',
                self.project + '/src/customer/site/theme/tests/test_viewlets.py',
                self.project + '/src/customer/site/theme/themes',
                self.project + '/src/customer/site/theme/themes/azul',
                self.project + '/src/customer/site/theme/themes/azul/css',
                self.project + '/src/customer/site/theme/themes/azul/css/plone.css',
                self.project + '/src/customer/site/theme/themes/azul/css/style.css',
                self.project + '/src/customer/site/theme/themes/azul/img',
                self.project + '/src/customer/site/theme/themes/azul/img/acesso-a-infornacao.png',
                self.project + '/src/customer/site/theme/themes/azul/img/background_footer.png',
                self.project + '/src/customer/site/theme/themes/azul/img/bg-acess-key.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/bg-menu-mobile-panel.png',
                self.project + '/src/customer/site/theme/themes/azul/img/bg-menu-mobile.png',
                self.project + '/src/customer/site/theme/themes/azul/img/border-hor.png',
                self.project + '/src/customer/site/theme/themes/azul/img/border-ver.png',
                self.project + '/src/customer/site/theme/themes/azul/img/brasil.png',
                self.project + '/src/customer/site/theme/themes/azul/img/bullet.png',
                self.project + '/src/customer/site/theme/themes/azul/img/cadeado.png',
                self.project + '/src/customer/site/theme/themes/azul/img/carta-comentarios.png',
                self.project + '/src/customer/site/theme/themes/azul/img/coala.jpeg',
                self.project + '/src/customer/site/theme/themes/azul/img/em-destaque.png',
                self.project + '/src/customer/site/theme/themes/azul/img/favicon.ico',
                self.project + '/src/customer/site/theme/themes/azul/img/flag-en.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/flag-es.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/header.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/icone-facebook.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/icone-facebook.png',
                self.project + '/src/customer/site/theme/themes/azul/img/icone-flickr.png',
                self.project + '/src/customer/site/theme/themes/azul/img/icone-related-items.png',
                self.project + '/src/customer/site/theme/themes/azul/img/icone-twitter.png',
                self.project + '/src/customer/site/theme/themes/azul/img/icone-youtube.png',
                self.project + '/src/customer/site/theme/themes/azul/img/mais_fotos.png',
                self.project + '/src/customer/site/theme/themes/azul/img/menu-ativo.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/menu-mobile-item.png',
                self.project + '/src/customer/site/theme/themes/azul/img/portlet-footer-textmore.png',
                self.project + '/src/customer/site/theme/themes/azul/img/portlet-header-expanded.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/portlet-header.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/readmoreblue.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmorebrown.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmoredarkblue.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmoredarkgray.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmoregray.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmoregreen.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmoreorange.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmorepurple.png',
                self.project + '/src/customer/site/theme/themes/azul/img/readmorewhiteblue.png',
                self.project + '/src/customer/site/theme/themes/azul/img/reportar-erros.png',
                self.project + '/src/customer/site/theme/themes/azul/img/search-buttom.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/search-button-30px.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/search-button.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/search-ico.png',
                self.project + '/src/customer/site/theme/themes/azul/img/sections-ico.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_cidadania_justica.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_ciencia_tecnologia.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_cultura.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_defesa_seguranca.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_economia_emprego.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_educacao.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_esporte.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_governo.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_infraestrutura.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_meio_ambiente.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_saude.png',
                self.project + '/src/customer/site/theme/themes/azul/img/seta_tursimo.png',
                self.project + '/src/customer/site/theme/themes/azul/img/shadow-bottom.gif',
                self.project + '/src/customer/site/theme/themes/azul/img/sprite-icons.png',
                self.project + '/src/customer/site/theme/themes/azul/img/sprite-setas.png',
                self.project + '/src/customer/site/theme/themes/azul/img/sprite.png',
                self.project + '/src/customer/site/theme/themes/azul/img/touch_icon.png',
                self.project + '/src/customer/site/theme/themes/azul/img/voltar-topo.png',
                self.project + '/src/customer/site/theme/themes/azul/index.html',
                self.project + '/src/customer/site/theme/themes/azul/js',
                self.project + '/src/customer/site/theme/themes/azul/js/menu.js',
                self.project + '/src/customer/site/theme/themes/azul/manifest.cfg',
                self.project + '/src/customer/site/theme/themes/azul/preview.png',
                self.project + '/src/customer/site/theme/themes/azul/rules.xml',
                self.project + '/src/customer/site/theme/upgrades',
                self.project + '/src/customer/site/theme/upgrades/__init__.py',
                self.project + '/src/customer/site/theme/upgrades/configure.zcml',
                self.project + '/src/customer/site/theme/upgrades/v1010',
                self.project + '/src/customer/site/theme/upgrades/v1010/__init__.py',
                self.project + '/src/customer/site/theme/upgrades/v1010/configure.zcml',
                self.project + '/src/customer/site/theme/upgrades/v1010/handler.py',
                self.project + '/src/customer/site/theme/upgrades/v1010/profile',
                self.project + '/src/customer/site/theme/upgrades/v1010/profile/metadata.xml',
            ]
        )
