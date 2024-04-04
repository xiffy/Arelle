from pathlib import PurePath, Path
from tests.integration_tests.validation.conformance_suite_config import ConformanceSuiteConfig, ConformanceSuiteAssetConfig

config = ConformanceSuiteConfig(
    args=[
        '--disclosureSystem', 'esef-unconsolidated-2021',
        '--formula', 'none',
    ],
    file='esef_conformance_suite_2021/esef_conformance_suite_2021/index_pure_xhtml.xml',
    assets=[
        ConformanceSuiteAssetConfig.conformance_suite(
            Path('esef_conformance_suite_2021.zip'),
            entry_point=Path('esef_conformance_suite_2021/esef_conformance_suite_2021/index_pure_xhtml.xml'),
            public_download_url='https://www.esma.europa.eu/sites/default/files/library/esef_conformance_suite_2021.zip',
        ),
    ],
    info_url='https://www.esma.europa.eu/document/conformance-suite-2021',
    local_filepath='esef_conformance_suite_2021.zip',
    name=PurePath(__file__).stem,
    network_or_cache_required=False,
    plugins=frozenset({'validate/ESEF'}),
    public_download_url='https://www.esma.europa.eu/sites/default/files/library/esef_conformance_suite_2021.zip',
    test_case_result_options='match-any',
)
