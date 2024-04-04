from pathlib import PurePath, Path
from tests.integration_tests.validation.conformance_suite_config import ConformanceSuiteConfig, ConformanceSuiteAssetConfig

config = ConformanceSuiteConfig(
    file='formula/tests/index.xml',
    assets=[
        ConformanceSuiteAssetConfig.conformance_suite(
            Path('formula.zip'),
            entry_point=Path('formula/tests/index.xml'),
        ),
    ],
    info_url='https://specifications.xbrl.org/release-history-formula-1.0-formula-conf.html',
    local_filepath='formula.zip',
    name=PurePath(__file__).stem,
    network_or_cache_required=False,
    shards=4,
    test_case_result_options='match-any',
)
