from pathlib import PurePath
from tests.integration_tests.validation.conformance_suite_config import ConformanceSuiteConfig

config = ConformanceSuiteConfig(
    args=[
        #'--formula', 'run',
    ],
    expected_failure_ids=frozenset(f'table-linkbase-conf-2015-08-12/conf/tests/{s}' for s in [
        '0100-table/0144-table-filter-arc/0144-table-filter-arc-testcase.xml:v-03',
        '0100-table/0144-table-filter-arc/0144-table-filter-arc-testcase.xml:v-04',
        #'0100-table/0144-table-filter-arc/0144-table-filter-arc-testcase.xml:v-05',
        '0100-table/0150-breakdown-without-aspects/0150-breakdown-without-aspects-testcase.xml:v-04',
        '0100-table/0150-breakdown-without-aspects/0150-breakdown-without-aspects-testcase.xml:v-04i',
        #'0100-table/0160-non-participating-aspects/0160-non-participating-aspects-testcase.xml:v-03',
        '0100-table/0170-parent-child-order/0170-parent-child-order-testcase.xml:v-01',
        '0200-table-parameters/0200-table-parameters-testcase.xml:v-02i',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-03',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-03i',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-04',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-04i',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-05',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-06',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-07',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-07i',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-07n',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-07ni',
        #'1000-rule-node/1000-rule-node-testcase.xml:v-08',
        #'1000-rule-node/1010-rule-node-concept-rule/1010-rule-node-concept-rule-testcase.xml:v-05',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-01',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-01i',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-02',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-02i',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-03',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-04',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-04i',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-06',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-06i',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-07',
        #'1000-rule-node/1020-rule-node-explicit-dimension-rule/1020-rule-node-explicit-dimension-rule-testcase.xml:v-07i',
        #'1000-rule-node/1030-rule-node-typed-dimension-rule/1030-rule-node-typed-dimension-rule-testcase.xml:v-01',
        #'1000-rule-node/1030-rule-node-typed-dimension-rule/1030-rule-node-typed-dimension-rule-testcase.xml:v-01i',
        #'1000-rule-node/1030-rule-node-typed-dimension-rule/1030-rule-node-typed-dimension-rule-testcase.xml:v-02',
        #'1000-rule-node/1030-rule-node-typed-dimension-rule/1030-rule-node-typed-dimension-rule-testcase.xml:v-02i',
        #'1000-rule-node/1030-rule-node-typed-dimension-rule/1030-rule-node-typed-dimension-rule-testcase.xml:v-03',
        '1000-rule-node/1030-rule-node-typed-dimension-rule/1030-rule-node-typed-dimension-rule-testcase.xml:v-03i',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-01',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-01i',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-02',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-02i',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-03',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-03i',
        #'1000-rule-node/1040-rule-node-period-rule/1040-rule-node-period-rule-testcase.xml:v-04',
        #'1000-rule-node/1050-rule-node-entity-rule/1050-rule-node-entity-rule-testcase.xml:v-01',
        #'1000-rule-node/1050-rule-node-entity-rule/1050-rule-node-entity-rule-testcase.xml:v-01i',
        #'1000-rule-node/1060-rule-node-unit-rule/1060-rule-node-unit-rule-testcase.xml:v-01',
        #'1000-rule-node/1060-rule-node-unit-rule/1060-rule-node-unit-rule-testcase.xml:v-01i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-01',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-01i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-02',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-02i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-03i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-04i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-05',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-05i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-06',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-06i',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-07',
        #'1000-rule-node/1070-rule-node-occ-rule/1070-rule-node-occ-rule-testcase.xml:v-07i',
        #'1000-rule-node/1100-abstract-rule-node/1100-abstract-rule-node-testcase.xml:v-01',
        #'1000-rule-node/1100-abstract-rule-node/1100-abstract-rule-node-testcase.xml:v-01i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-01',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-01i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-02',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-02i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-03',
        '1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-03i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-04',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-04i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-05',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-05i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-09',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-09i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-10',
        '1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-10i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-11',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-11i',
        #'1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-12',
        '1000-rule-node/1200-merged-rule-node/1200-merged-rule-node-testcase.xml:v-12i',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-01',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-01i',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-06',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-06i',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-07',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-07i',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-08',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-08i',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-09',
        #'1000-rule-node/1300-rule-node-rule-sets/1300-rule-node-rule-sets-testcase.xml:v-10',
        #'3100-concept-relationship-node/3100-concept-relationship-node-testcase.xml:v-01',
        #'3100-concept-relationship-node/3100-concept-relationship-node-testcase.xml:v-02',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-01',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-01i',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-02',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-02i',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-03',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-03i',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-04',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-04i',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-06',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-07',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-08',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-08i',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-09',
        #'3100-concept-relationship-node/3110-concept-relationship-node-relationship-source/3110-concept-relationship-node-relationship-source-testcase.xml:v-09i',
        #'3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-01',
        #'3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-01i',
        '3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-02',
        #'3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-03',
        #'3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-04',
        #'3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-05',
        #'3100-concept-relationship-node/3120-concept-relationship-node-linkrole/3120-concept-relationship-node-linkrole-testcase.xml:v-06',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-01',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-01i',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-02',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-02i',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-03',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-03i',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-04',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-05',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-06',
        #'3100-concept-relationship-node/3130-concept-relationship-node-arcrole/3130-concept-relationship-node-arcrole-testcase.xml:v-07',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-01',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-01i',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-02',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-02i',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-03',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-03i',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-04',
        #'3100-concept-relationship-node/3140-concept-relationship-node-linkname/3140-concept-relationship-node-linkname-testcase.xml:v-05',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-01',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-01i',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-02',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-02i',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-03',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-03i',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-04',
        #'3100-concept-relationship-node/3150-concept-relationship-node-arcname/3150-concept-relationship-node-arcname-testcase.xml:v-05',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-01',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-01i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-02',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-02i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-03',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-03i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-04',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-04i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-05',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-05i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-06',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-06i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-07',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-07i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-08',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-08i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-08a',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-08ai',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-09',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-09i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-10',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-10i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-11',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-11i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-12',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-12i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-13',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-14',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-15',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-15i',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-16',
        #'3100-concept-relationship-node/3160-concept-relationship-node-formula-axis/3160-concept-relationship-node-formula-axis-testcase.xml:v-17',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-01',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-01i',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-02',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-02i',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-03',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-03i',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-04',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-05',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-05i',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-06',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-07',
        #'3100-concept-relationship-node/3170-concept-relationship-node-generations/3170-concept-relationship-node-generations-testcase.xml:v-08',
        #'3100-concept-relationship-node/3180-concept-relationship-node-tag-selectors/3180-concept-relationship-node-tag-selectors-testcase.xml:v-01',
        #'3100-concept-relationship-node/3180-concept-relationship-node-tag-selectors/3180-concept-relationship-node-tag-selectors-testcase.xml:v-02',
        #'3100-concept-relationship-node/3180-concept-relationship-node-tag-selectors/3180-concept-relationship-node-tag-selectors-testcase.xml:v-03',
        #'3200-dimension-relationship-node/3200-dimension-relationship-node-testcase.xml:v-01',
        #'3200-dimension-relationship-node/3200-dimension-relationship-node-testcase.xml:v-01i',
        #'3200-dimension-relationship-node/3200-dimension-relationship-node-testcase.xml:v-02',
        #'3200-dimension-relationship-node/3200-dimension-relationship-node-testcase.xml:v-03',
        #'3200-dimension-relationship-node/3200-dimension-relationship-node-testcase.xml:v-03i',
        #'3200-dimension-relationship-node/3200-dimension-relationship-node-testcase.xml:v-04',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-01',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-01i',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-02',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-02i',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-03',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-03i',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-08',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-08i',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-09',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-09i',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-10',
        #'3200-dimension-relationship-node/3210-dimension-relationship-node-relationship-source/3210-dimension-relationship-node-relationship-source-testcase.xml:v-11',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-01',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-01i',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-02',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-02i',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-03',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-04',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-05',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-06',
        #'3200-dimension-relationship-node/3220-dimension-relationship-node-linkrole/3220-dimension-relationship-node-linkrole-testcase.xml:v-07',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-01',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-01i',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-02',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-02i',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-03',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-03i',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-04',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-04i',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-05',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-05i',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-06',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-06i',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-07',
        #'3200-dimension-relationship-node/3240-dimension-relationship-node-formula-axis/3240-dimension-relationship-node-formula-axis-testcase.xml:v-08',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-01',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-01i',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-02',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-02i',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-03',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-03i',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-04',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-05',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-05i',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-06',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-07',
        #'3200-dimension-relationship-node/3250-dimension-relationship-node-generations/3250-dimension-relationship-node-generations-testcase.xml:v-08',
        '6000-aspect-node/6000-aspect-node-testcase.xml:v-01',
        '6000-aspect-node/6000-aspect-node-testcase.xml:v-02',
        #'6000-aspect-node/6000-aspect-node-testcase.xml:v-03',
        #'6000-aspect-node/6000-aspect-node-testcase.xml:v-04',
        #'6000-aspect-node/6100-concept-aspect-node/6100-concept-aspect-node-testcase.xml:v-01',
        #'6000-aspect-node/6100-concept-aspect-node/6100-concept-aspect-node-testcase.xml:v-01i',
        #'6000-aspect-node/6200-period-aspect-node/6200-period-aspect-node-testcase.xml:v-01',
        #'6000-aspect-node/6200-period-aspect-node/6200-period-aspect-node-testcase.xml:v-01i',
        #'6000-aspect-node/6300-entity-identifier-aspect-node/6300-entity-identifier-aspect-node-testcase.xml:v-01',
        '6000-aspect-node/6300-entity-identifier-aspect-node/6300-entity-identifier-aspect-node-testcase.xml:v-01i',
        #'6000-aspect-node/6400-unit-aspect-node/6400-unit-aspect-node-testcase.xml:v-01',
        #'6000-aspect-node/6400-unit-aspect-node/6400-unit-aspect-node-testcase.xml:v-01i',
        #'6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-01',
        #'6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-01i',
        #'6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-02',
        '6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-02i',
        '6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-03',
        #'6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-03i',
        #'6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-05',
        #'6000-aspect-node/6500-dimension-aspect-node/6500-dimension-aspect-node-testcase.xml:v-06',
        #'6000-aspect-node/6600-aspect-node-concept-filter/6600-aspect-node-concept-filter-testcase.xml:v-01',
        #'6000-aspect-node/6600-aspect-node-concept-filter/6600-aspect-node-concept-filter-testcase.xml:v-02',
        #'6000-aspect-node/6610-aspect-node-period-filter/6610-aspect-node-period-filter-testcase.xml:v-01',
        #'6000-aspect-node/6610-aspect-node-period-filter/6610-aspect-node-period-filter-testcase.xml:v-02',
        #'6000-aspect-node/6610-aspect-node-period-filter/6610-aspect-node-period-filter-testcase.xml:v-03',
        '6000-aspect-node/6610-aspect-node-period-filter/6610-aspect-node-period-filter-testcase.xml:v-04',
        #'6000-aspect-node/6610-aspect-node-period-filter/6610-aspect-node-period-filter-testcase.xml:v-05',
        #'6000-aspect-node/6610-aspect-node-period-filter/6610-aspect-node-period-filter-testcase.xml:v-06',
        #'6000-aspect-node/6620-aspect-node-entity-filter/6620-aspect-node-entity-filter-testcase.xml:v-01',
        #'6000-aspect-node/6620-aspect-node-entity-filter/6620-aspect-node-entity-filter-testcase.xml:v-02',
        #'6000-aspect-node/6630-aspect-node-unit-filter/6630-aspect-node-unit-filter-testcase.xml:v-01',
        #'6000-aspect-node/6630-aspect-node-unit-filter/6630-aspect-node-unit-filter-testcase.xml:v-02',
        #'6000-aspect-node/6630-aspect-node-unit-filter/6630-aspect-node-unit-filter-testcase.xml:v-03',
        #'6000-aspect-node/6640-aspect-node-explicit-dimension-filter/6640-aspect-node-explicit-dimension-filter-testcase.xml:v-01',
        #'6000-aspect-node/6640-aspect-node-explicit-dimension-filter/6640-aspect-node-explicit-dimension-filter-testcase.xml:v-02',
        #'6000-aspect-node/6640-aspect-node-explicit-dimension-filter/6640-aspect-node-explicit-dimension-filter-testcase.xml:v-03',
        #'6000-aspect-node/6650-aspect-node-typed-dimension-filter/6650-aspect-node-typed-dimension-filter-testcase.xml:v-01',
        #'6000-aspect-node/6650-aspect-node-typed-dimension-filter/6650-aspect-node-typed-dimension-filter-testcase.xml:v-02',
        #'6000-aspect-node/6650-aspect-node-typed-dimension-filter/6650-aspect-node-typed-dimension-filter-testcase.xml:v-03',
        #'6000-aspect-node/6650-aspect-node-typed-dimension-filter/6650-aspect-node-typed-dimension-filter-testcase.xml:v-04',
        #'6000-aspect-node/6650-aspect-node-typed-dimension-filter/6650-aspect-node-typed-dimension-filter-testcase.xml:v-04i',
        '6000-aspect-node/6660-aspect-node-aspect-cover-filter/6660-aspect-node-aspect-cover-filter-testcase.xml:v-01',
    ]),
    file='table-linkbase-conf-2015-08-12/conf/testcases-index.xml',
    info_url='https://specifications.xbrl.org/work-product-index-table-linkbase-table-linkbase-1.0.html',
    local_filepath='table-linkbase-conf-2015-08-12.zip',
    name=PurePath(__file__).stem,
    network_or_cache_required=False,
    public_download_url='https://www.xbrl.org/2015/table-linkbase-conf-2015-08-12.zip',
    shards=4,
    test_case_result_options='match-any',
)
