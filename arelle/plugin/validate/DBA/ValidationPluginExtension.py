"""
See COPYRIGHT.md for copyright information.
"""
from __future__ import annotations

from arelle.ModelValue import qname
from arelle.ValidateXbrl import ValidateXbrl
from arelle.typing import TypeGetText
from arelle.utils.validate.ValidationPlugin import ValidationPlugin
from .PluginValidationDataExtension import PluginValidationDataExtension

import re

_: TypeGetText

DANISH_CURRENCY_ID = 'DKK'
NAMESPACE_ARR = 'http://xbrl.dcca.dk/arr'
NAMESPACE_CMN = 'http://xbrl.dcca.dk/cmn'
NAMESPACE_FSA = 'http://xbrl.dcca.dk/fsa'
NAMESPACE_GSD = 'http://xbrl.dcca.dk/gsd'
NAMESPACE_SOB = 'http://xbrl.dcca.dk/sob'
PERSONNEL_EXPENSE_THRESHOLD = 200000
ROUNDING_MARGIN = 1000


class ValidationPluginExtension(ValidationPlugin):
    def newPluginData(self, validateXbrl: ValidateXbrl) -> PluginValidationDataExtension:
        return PluginValidationDataExtension(
            self.name,
            accountingPolicyConceptQns=frozenset([
                qname(f'{{{NAMESPACE_FSA}}}DescriptionMethodsOfRecognitionAndMeasurementBasisForCashFlowsStatement'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfAccountingPoliciesRelatedToDerivativeFinancialInstruments'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfAnyFailureOfApplyingEliminationBetweenConsolidatedEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfChangeInInventoriesOfFinishedGoodsWorkInProgressAndGoodsForResale'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfChangesInCompositionOfEntityActivities'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfEffectOfChangeInAccountingEstimatesOnAssetsLiabilitiesEquityFinancialPositionAndResults'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfEffectOfChangeInRecognitionAndMeasurementBasisOfAssetsAndLiabilitiesAsResultOfErrors'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfEffectOfDerogationFromProvisionsOfDanishFinancialStatementsActOnAssetsLiabilitiesEquityFinancialPositionAndResults'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfGeneralMattersRelatedToRecognitionMeasurementAndChangesInAccountingPolicies'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfImpairmentOfFinancialAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfIncomeFromOtherInvestmentsAndReceivablesThatAreFixedAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfKeyFiguresAndFinancialRatios'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfAmortisationOfNoncurrentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfAssetsMeantForSale'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfCurrentTaxReceivablesAndLiabilities'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfDividends'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfForeignCurrencies'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfHedgingRecognisedExpectedToReceiveAndAssumedAssetsAndLiabilities'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfImpairmentLossesAndDepreciation'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfIncomeExceedCostAndCostExceedsIncomeForTheFinancialYear'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfInvestmentsAsCurrentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfLeases'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfLiquidationAccount'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfPrepayments'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisForDistributions'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisForInvestmentsInJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisForInvestmentsInSubsidiariesAndAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisIncludingBasesUsedForRevaluationsDepreciationAmortisationEstimatedResidualValueUsefulLifeWritedownsUpwardAndDownwardAdjustments'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfAdministrativeExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfAssetsAndLiabilities'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfCashAndCashEquivalents'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfContractWorkInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfCostOfProduction'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfCostOfSales'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfDeferredIncomeAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfDeferredIncomeLiabilities'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfDistributionCosts'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfEmployeeBenefitExpense'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfEquity'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfExpensesFromInvestmentsInGroupEnterprisesAndAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfExternalExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfFinanceExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfFinanceIncome'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfFinanceIncomeAndExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfGainsLossesFromCurrentValueAdjustmentsOfBiologicalAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfGainsLossesFromCurrentValueAdjustmentsOfInvestmentProperty'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfGainsLossesFromCurrentValueAdjustmentsOfOtherInvestmentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfGrossProfitLoss'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIncomeAndExpensesFromInvestmentsInGroupEnterprisesAndAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIncomeAndExpensesFromInvestmentsInJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIncomeFromInvestmentsInGroupEnterprisesAndAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIncomeStatementItems'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIndirectCostsOfProductionRecognisedUnderAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfInventories'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfInvestmentProperty'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfLeaseholdImprovements'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfLiabilitiesOtherThanProvisions'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfOtherInvestmentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfOtherOperatingExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfOtherOperatingIncome'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfOtherOperatingIncomeAndExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfOtherProvisions'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfPropertyCosts'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfPropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfProvisions'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfResearchAndDevelopmentExpendituresRecognisedAsExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfRevenue'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfSpecialItems'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfTaxExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfTaxPayablesAndDeferredTax'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisUsedAtEstablishment'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfRecognitionAndMeasurementBasisUsedInBusinessCombinations'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfStatingKeyFiguresAndFinancialRatiosIncludedInManagementReview'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfMethodsOfTranslationOfForeignCurrencies'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfOtherKeyFiguresAndFinancialRatios'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfOtherTaxExpenses'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfOwnWorkCapitalised'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfPublicGrants'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfRawMaterialsAndConsumablesUsed'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfRecognitionAndMeasurementBasisForDiscontinuedOperationsBalanceSheet'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfRemainingPositiveOrNegativeBalancesRelatedToAcquisitionAndUnitingOfInterestsAndMethodsUsedInConnectionWithTheirCalculation'),
                qname(f'{{{NAMESPACE_FSA}}}DescriptionOfWritedownsOfCurrentAssetsThatExceedNormalWritedowns'),
                qname(f'{{{NAMESPACE_FSA}}}DisclosureOfTrueAndFairViewAndGoingConcern'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfAmortizationPeriodForGoodwill'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfAssumptionsOnWhichChosenCalculationMethodHasBeenBasedForFinancialAssetsAndLiabilitiesMeasuredAtNetPresentValueOrAmortisedCost'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfAssumptionsOnWhichChosenCalculationMethodHasBeenBasedForInvestmentsAndBiologicalAssetsMeasuredAtFairValue'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfBasisOnWhichEquityInvestmentsInSubsidiariesAndAssociatesHaveBeenRecognisedAtCost'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfChangeInAccountingEstimates'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfChangeInRecognitionAndMeasurementBasisOfAssetsAndLiabilitiesAsResultOfErrors'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfDerogationFromProvisionsOfDanishFinancialStatementsActOnAssetsLiabilitiesEquityFinancialPositionAndResults'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfDifferenceInBalanceSheetDatesBetweenParentAndConsolidatedSubsidiariesAndDescriptionOfImportantEventsOccurringAtThatTime'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfDifferenceInMethodsOfRecognitionAndMeasurementBasisBetweenParentAndConsolidatedGroupEnterprise'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfEntitysDefinitionOfCashAndCashEquivalents'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfGroundsOfNoncomparabilityOrRestatement'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfNotDisclosingInformationOnAGroupEntity'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfOtherMethodsOfRecognitionAndMeasurementBasisForAssetsInPreviousPeriod'),
                qname(f'{{{NAMESPACE_FSA}}}ExplanationOfWhetherInterestIsIncludedInCost'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnChangesAndEffectsOfChangesOnRecognitionAndMeasurementBasisResultingFromChangesInAccountingEstimatesOrErrors'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnConsolidatedResultsAndEquityIfSubsidiaryHasNotBeenPreviouslyIncludedInConsolidatedFinancialStatementsAndParentHoldsInvestmentsInSubsidiarySolelyWithViewToItsSubsequentTransfer'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnConsolidations'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnHedging'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnIncentivePrograms'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnIntragroupTransactions'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnLeasingContracts'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnMinorityInterests'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnNoncomparabilityOrRestatement'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnOmissionOfConsolidatedFinancialStatement'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnReportingClassOfEntity'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnSegments'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnSignificantUncertainties'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnSpecificPrerequisitesRegardingDevelopmentProjectsAndTaxAssets'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnSubsequentEvents'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnSubsidiariesHavingPresentedTheAnnualReportEtcWithReferenceToTheDanishFinancialStatementsAct78aConcerningTheExceptionForReportingClassCMediumsizeSubsidiariesWhichChoosesToPresentTheAnnualReportEtcAccordingToReportingClassB'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnThePrincipalModificationsAsResultOfTheLiquidation'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnTimingDifferencesInCustomerPaymentsEspeciallyForUtilities'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnTreatmentOfAdditionalPaymentsFromAndRepaymentsToRelatedParties'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnTrueAndFairViewIfProvisionsOfDanishFinancialStatementsActAreNotSufficient'),
                qname(f'{{{NAMESPACE_FSA}}}InformationOnUncertaintiesRelatingToGoingConcern'),
                qname(f'{{{NAMESPACE_FSA}}}SubsidiariesHasPresentedTheAnnualReportEtc.WithReferenceToTheDanishFinancialStatementsAct78aConcerningTheExceptionForReportingClassCMediumsizeSubsidiariesWhichChoosesToPresentTheAnnualReportEtcAccordingToReportingClassB'),
            ]),
            annualReportTypes=frozenset([
                'Årsrapport',
                'årsrapport',
                'Annual report'
            ]),
            assetsQn=qname(f'{{{NAMESPACE_FSA}}}Assets'),
            auditedAssuranceReportsDanish='Andre erklæringer med sikkerhed',
            auditedAssuranceReportsEnglish='The independent auditor\'s reports (Other assurance Reports)',
            auditedExtendedReviewDanish='Erklæring om udvidet gennemgang',
            auditedExtendedReviewEnglish='Auditor\'s report on extended review',
            auditedFinancialStatementsDanish='Revisionspåtegning',
            auditedFinancialStatementsEnglish='Auditor\'s report on audited financial statements',
            auditedNonAssuranceReportsDanish='Andre erklæringer uden sikkerhed',
            auditedNonAssuranceReportsEnglish='Auditor\'s reports (Other non-assurance reports)',
            averageNumberOfEmployeesQn=qname(f'{{{NAMESPACE_FSA}}}AverageNumberOfEmployees'),
            balanceSheetQnLessThanOrEqualToAssets=frozenset([
                qname(f'{{{NAMESPACE_FSA}}}NoncurrentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}IntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}CompletedDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}ConcessionsOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}PatentsOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}TrademarksOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}OtherSimilarRightsOriginatingFromDevelopmentProjects'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredConcessions'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredPatents'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredLicences'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredTrademarks'),
                qname(f'{{{NAMESPACE_FSA}}}AcquiredOtherSimilarRights'),
                qname(f'{{{NAMESPACE_FSA}}}Goodwill'),
                qname(f'{{{NAMESPACE_FSA}}}DevelopmentProjectsInProgressAndPrepaymentsForIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DevelopmentProjectsInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}PrepaymentsForIntangibleAssets'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}LandAndBuildings'),
                qname(f'{{{NAMESPACE_FSA}}}Land'),
                qname(f'{{{NAMESPACE_FSA}}}Buildings'),
                qname(f'{{{NAMESPACE_FSA}}}InvestmentProperty'),
                qname(f'{{{NAMESPACE_FSA}}}OtherInvestmentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}PlantAndMachinery'),
                qname(f'{{{NAMESPACE_FSA}}}FixturesFittingsToolsAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}BiologicalAssets'),
                qname(f'{{{NAMESPACE_FSA}}}LeaseholdImprovements'),
                qname(f'{{{NAMESPACE_FSA}}}Ships'),
                qname(f'{{{NAMESPACE_FSA}}}Planes'),
                qname(f'{{{NAMESPACE_FSA}}}RightofuseAssets'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyPlantAndEquipmentInProgressAndPrepaymentsForPropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyPlantAndEquipmentInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}PrepaymentsForPropertyPlantAndEquipment'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsAndReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsInGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsInAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermInvestmentsInJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}OtherLongtermInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}OtherLongtermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}LongtermReceivablesFromOwnersAndManagement'),
                qname(f'{{{NAMESPACE_FSA}}}NoncurrentDeferredTaxAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DepositsLongtermInvestmentsAndReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}CostExceedsIncomeForTheFinancialYearLongtermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ContributedCapitalInArrearsLongTerm'),
                qname(f'{{{NAMESPACE_FSA}}}NoncurrentContractAssets'),
                qname(f'{{{NAMESPACE_FSA}}}CurrentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}Inventories'),
                qname(f'{{{NAMESPACE_FSA}}}RawMaterialsAndConsumables'),
                qname(f'{{{NAMESPACE_FSA}}}WorkInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}ManufacturedGoodsAndGoodsForResale'),
                qname(f'{{{NAMESPACE_FSA}}}PrepaymentsForGoods'),
                qname(f'{{{NAMESPACE_FSA}}}Livestock'),
                qname(f'{{{NAMESPACE_FSA}}}PropertyHeldForSaleInTheOrdinaryCourseOfBusiness'),
                qname(f'{{{NAMESPACE_FSA}}}AssetsHeldForSaleInventories'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermTradeReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ContractWorkInProgress'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromAssociates'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromJointVentures'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesDividendsFromParticipatingInterests'),
                qname(f'{{{NAMESPACE_FSA}}}CurrentDeferredTaxAssets'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermTaxReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermTaxReceivablesFromGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}VatAndDutiesReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}OtherShorttermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}ContributedCapitalInArrears'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermReceivablesFromOwnersAndManagement'),
                qname(f'{{{NAMESPACE_FSA}}}DeferredIncomeAssets'),
                qname(f'{{{NAMESPACE_FSA}}}CostExceedsIncomeForTheFinancialYearShorttermReceivables'),
                qname(f'{{{NAMESPACE_FSA}}}TimingDifferencesShorttermReceivablesEspeciallyUtilities'),
                qname(f'{{{NAMESPACE_FSA}}}CurrentContractAssets'),
                qname(f'{{{NAMESPACE_FSA}}}DerivativeFinancialInstrumentsShorttermAssets'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}ShorttermInvestmentsInGroupEnterprises'),
                qname(f'{{{NAMESPACE_FSA}}}OtherShorttermInvestments'),
                qname(f'{{{NAMESPACE_FSA}}}CashAndCashEquivalents'),
                qname(f'{{{NAMESPACE_FSA}}}AssetsMeantForSale'),
            ]),
            basisForAdverseOpinionDanish='Grundlag for afkræftende konklusion',
            basisForAdverseOpinionEnglish='Basis for Adverse Opinion',
            basisForDisclaimerOpinionDanish='Grundlag for manglende konklusion',
            basisForDisclaimerOpinionEnglish='Basis for Disclaimer of Opinion',
            basisForQualifiedOpinionDanish='Grundlag for konklusion med forbehold',
            basisForQualifiedOpinionEnglish='Basis for Qualified Opinion',
            classOfReportingEntityQn=qname(f'{{{NAMESPACE_FSA}}}ClassOfReportingEntity'),
            consolidatedMemberQn=qname(f'{{{NAMESPACE_CMN}}}ConsolidatedMember'),
            consolidatedSoloDimensionQn=qname(f'{{{NAMESPACE_CMN}}}ConsolidatedSoloDimension'),
            cpr_regex=re.compile(r'^([0-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}-[0-9]{4}'),
            dateOfApprovalOfAnnualReportQn=qname(f'{{{NAMESPACE_SOB}}}DateOfApprovalOfAnnualReport'),
            dateOfExtraordinaryDividendDistributedAfterEndOfReportingPeriod=qname(f'{{{NAMESPACE_FSA}}}DateOfExtraordinaryDividendDistributedAfterEndOfReportingPeriod'),
            dateOfGeneralMeetingQn=qname(f'{{{NAMESPACE_GSD}}}DateOfGeneralMeeting'),
            descriptionOfQualificationsOfAssuranceEngagementPerformedQn=qname(f'{{{NAMESPACE_ARR}}}DescriptionOfQualificationsOfAssuranceEngagementPerformed'),
            descriptionOfQualificationsOfAuditedFinancialStatementsQn=qname(f'{{{NAMESPACE_ARR}}}DescriptionOfQualificationsOfAuditedFinancialStatements'),
            descriptionOfQualificationsOfFinancialStatementsExtendedReviewQn=qname(f'{{{NAMESPACE_ARR}}}DescriptionOfQualificationsOfFinancialStatementsExtendedReview'),
            descriptionsOfQualificationsOfReviewedFinancialStatementsQn=qname(f'{{{NAMESPACE_ARR}}}DescriptionsOfQualificationsOfReviewedFinancialStatements'),
            distributionOfResultsQns=frozenset([
                qname(f'{{{NAMESPACE_FSA}}}DistributionsResultDistribution'),
                qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryDistributions'),
                qname(f'{{{NAMESPACE_FSA}}}ProposedDividendRecognisedInEquity'),
                qname(f'{{{NAMESPACE_FSA}}}ProposedExtraordinaryDividendRecognisedInEquity'),
                qname(f'{{{NAMESPACE_FSA}}}ProposedExtraordinaryDividendRecognisedInLiabilities'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredFromToHedgeFund'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredFromToReserveFund'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredFromToReservesAvailable'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromEquityAttributableToParent'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromMinorityInterests'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromOtherStatutoryReserves'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromReserveAccordingToArticlesOfAssociation'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromReserveForNetRevaluationAccordingToEquityMethod'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromReserveForNetRevaluationOfInvestmentAssets'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromRestOfOtherReserves'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToFromRetainedEarnings'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForCurrentValueAdjustmentsOfCurrencyGains'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForCurrentValueOfHedging'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForDevelopmentExpenditure'),
                qname(f'{{{NAMESPACE_FSA}}}TransferredToReserveForEntrepreneurialCompany'),
            ]),
            employeeBenefitsExpenseQn=qname(f'{{{NAMESPACE_FSA}}}EmployeeBenefitsExpense'),
            equityQn=qname(f'{{{NAMESPACE_FSA}}}Equity'),
            extraordinaryCostsQn=qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryCosts'),
            extraordinaryIncomeQn=qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryIncome'),
            extraordinaryResultBeforeTaxQn=qname(f'{{{NAMESPACE_FSA}}}ExtraordinaryResultBeforeTax'),
            fr37RestrictedText='has not given rise to reservations',
            hasNotGivenRiseToReservationsText=frozenset([
                'har ikke givet anledning til forbehold',
                'has not given rise to reservations',
            ]),
            identificationNumberCvrOfAuditFirmQn=qname(f'{{{NAMESPACE_CMN}}}IdentificationNumberCvrOfAuditFirm'),
            independentAuditorsReportDanish='Den uafhængige revisors erklæringer (review)',
            independentAuditorsReportEnglish='The independent auditor\'s reports (Review)',
            informationOnTypeOfSubmittedReportQn=qname(f'{{{NAMESPACE_GSD}}}InformationOnTypeOfSubmittedReport'),
            liabilitiesQn=qname(f'{{{NAMESPACE_FSA}}}LiabilitiesAndEquity'),
            liabilitiesAndEquityQn=qname(f'{{{NAMESPACE_FSA}}}LiabilitiesAndEquity'),
            liabilitiesOtherThanProvisionsQn=qname(f'{{{NAMESPACE_FSA}}}LiabilitiesOtherThanProvisions'),
            longtermLiabilitiesOtherThanProvisionsQn=qname(f'{{{NAMESPACE_FSA}}}LongtermLiabilitiesOtherThanProvisions'),
            managementEndorsementQns=frozenset([
                qname(f'{{{NAMESPACE_SOB}}}StatementByExecutiveAndSupervisoryBoards'),
                qname(f'{{{NAMESPACE_SOB}}}TheReportingEntityAppliesTheExceptionConcerningOptingOutOfTheStatementByManagementEtc'),
                qname(f'{{{NAMESPACE_SOB}}}IdentificationOfApprovedAnnualReport'),
                qname(f'{{{NAMESPACE_SOB}}}ConfirmationThatAnnualReportIsPresentedInAccordanceWithRequirementsProvidedForByLegislationAnyStandardsAndRequirementsProvidedByArticlesOfAssociationOrByAgreement'),
                qname(f'{{{NAMESPACE_SOB}}}ConfirmationThatFinancialStatementGivesTrueAndFairViewOfAssetsLiabilitiesEquityFinancialPositionAndResults'),
                qname(f'{{{NAMESPACE_SOB}}}ConfirmationThatSupplementaryReportsGiveTrueAndFairViewInAccordanceWithGenerallyAcceptedGuidelinesForSuchReports'),
                qname(f'{{{NAMESPACE_SOB}}}ManagementsStatementAboutManagementsReview'),
                qname(f'{{{NAMESPACE_SOB}}}RecommendationForApprovalOfAnnualReportByGeneralMeeting'),
                qname(f'{{{NAMESPACE_SOB}}}DateOfApprovalOfAnnualReport'),
                qname(f'{{{NAMESPACE_SOB}}}PlaceOfSignatureOfStatement'),
                qname(f'{{{NAMESPACE_CMN}}}NameAndSurnameOfMemberOfExecutiveBoard'),
                qname(f'{{{NAMESPACE_CMN}}}TitleOfMemberOfExecutiveBoard'),
                qname(f'{{{NAMESPACE_CMN}}}DescriptionOfMemberOfExecutiveBoard'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfObjectionsOfMemberOfExecutiveBoardOnAnnualReport'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfSpecificAndAdequateGroundsForObjectionsOfMemberOfExecutiveBoardOnAnnualReport'),
                qname(f'{{{NAMESPACE_CMN}}}NameAndSurnameOfMemberOfSupervisoryBoard'),
                qname(f'{{{NAMESPACE_CMN}}}TitleOfMemberOfSupervisoryBoard'),
                qname(f'{{{NAMESPACE_CMN}}}DescriptionOfMemberOfSupervisoryBoard'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfObjectionsOfMemberOfSupervisoryBoardOnAnnualReport'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfSpecificAndAdequateGroundsForObjectionsOfMemberOfSupervisoryBoardOnAnnualReport'),
                qname(f'{{{NAMESPACE_SOB}}}IdentificationNumberCVRofParticipantNotPartOfTheRegisteredManagementMemberOfSupervisoryBoard'),
                qname(f'{{{NAMESPACE_SOB}}}NameOfEntityParticipantNotPartOfTheRegisteredManagementMemberOfSupervisoryBoard'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfParticipantNotPartOfTheRegisteredManagementMemberOfSupervisoryBoard'),
                qname(f'{{{NAMESPACE_GSD}}}NameAndSurnameOfMemberOfSupervisoryCommittee'),
                qname(f'{{{NAMESPACE_GSD}}}TitleOfMemberOfSupervisoryCommittee'),
                qname(f'{{{NAMESPACE_GSD}}}DescriptionOfMemberOfSupervisoryCommittee'),
                qname(f'{{{NAMESPACE_GSD}}}NameAndSurnameOfMemberOfSupervisoryCommittee'),
                qname(f'{{{NAMESPACE_GSD}}}TitleOfMemberOfSupervisoryCommittee'),
                qname(f'{{{NAMESPACE_CMN}}}NameAndSurnameOfLiquidator'),
                qname(f'{{{NAMESPACE_CMN}}}TitleOfLiquidator'),
                qname(f'{{{NAMESPACE_CMN}}}DescriptionOfLikvidator'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfObjectionsOfLiquidatorOnAnnualReport'),
                qname(f'{{{NAMESPACE_SOB}}}DescriptionOfSpecificAndAdequateGroundsForObjectionsOfLiquidatorOnAnnualReport'),
            ]),
            noncurrentAssetsQn=qname(f'{{{NAMESPACE_FSA}}}NoncurrentAssets'),
            nameAndSurnameOfChairmanOfGeneralMeetingQn=qname(f'{{{NAMESPACE_GSD}}}NameAndSurnameOfChairmanOfGeneralMeeting'),
            nameOfAuditFirmQn=qname(f'{{{NAMESPACE_CMN}}}NameOfAuditFirm'),
            otherEmployeeExpenseQn=qname(f'{{{NAMESPACE_FSA}}}OtherEmployeeExpense'),
            positiveProfitThreshold=1000,
            postemploymentBenefitExpenseQn=qname(f'{{{NAMESPACE_FSA}}}PostemploymentBenefitExpense'),
            precedingReportingPeriodEndDateQn=qname(f'{{{NAMESPACE_GSD}}}PredingReportingPeriodEndDate'),  # Typo in taxonomy
            precedingReportingPeriodStartDateQn=qname(f'{{{NAMESPACE_GSD}}}PrecedingReportingPeriodStartDate'),
            profitLossQn=qname(f'{{{NAMESPACE_FSA}}}ProfitLoss'),
            proposedDividendRecognisedInEquityQn=qname(f'{{{NAMESPACE_FSA}}}ProposedDividendRecognisedInEquity'),
            proposedExtraordinaryDividendRecognisedInLiabilitiesQn=qname(f'{{{NAMESPACE_FSA}}}ProposedExtraordinaryDividendRecognisedInLiabilities'),
            provisionsQn=qname(f'{{{NAMESPACE_FSA}}}Provisions'),
            reportingPeriodEndDateQn=qname(f'{{{NAMESPACE_GSD}}}ReportingPeriodEndDate'),
            reportingPeriodStartDateQn=qname(f'{{{NAMESPACE_GSD}}}ReportingPeriodStartDate'),
            shorttermLiabilitiesOtherThanProvisionsQn=qname(f'{{{NAMESPACE_FSA}}}ShorttermLiabilitiesOtherThanProvisions'),
            signatureOfAuditorsDateQn=qname(f'{{{NAMESPACE_ARR}}}SignatureOfAuditorsDate'),
            taxExpenseOnOrdinaryActivitiesQn=qname(f'{{{NAMESPACE_FSA}}}TaxExpenseOnOrdinaryActivities'),
            taxExpenseQn=qname(f'{{{NAMESPACE_FSA}}}TaxExpense'),
            typeOfAuditorAssistanceQn=qname(f'{{{NAMESPACE_CMN}}}TypeOfAuditorAssistance'),
            typeOfBasisForModifiedOpinionOnFinancialStatementsReviewQn=qname(f'{{{NAMESPACE_ARR}}}TypeOfBasisForModifiedOpinionOnFinancialStatementsReview'),
            typeOfReportingPeriodDimensionQn=qname(f'{{{NAMESPACE_GSD}}}TypeOfReportingPeriodDimension'),
            wagesAndSalariesQn=qname(f'{{{NAMESPACE_FSA}}}WagesAndSalaries'),
        )
