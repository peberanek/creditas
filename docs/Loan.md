# Loan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_id** | **str** | The unique identifier for the loan | [optional] 
**bban** | **str** | BBAN (Basic Bank Account Number) The country-specific account number associated with the loan | [optional] 
**bank_code** | **str** | The country-specific bank code for the account associated with the loan | [optional] 
**iban** | **str** | IBAN (International Bank Account Number) | [optional] 
**bic** | **str** | BIC (Business Identification Code) - International unique identifier for the bank | [optional] 
**currency** | **str** | The loan account&#39;s currency code in ISO 4217 format (CZK, EUR, USD, ...) | [optional] 
**country** | **str** | The country code of the loan account&#39;s origin in ISO 3166-1 alpha-3 format (CZE, SVK, ...) | [optional] 
**status** | **str** | The status of the loan (ACTIVE, INACTIVE, CLOSED, TO_BE_CLOSED) | [optional] 
**name** | **str** | The name (description) for the loan (typically the name of the account&#39;s owner) | [optional] 
**alias** | **str** | The consumer preferred loan name | [optional] 
**product_i18_n** | **str** | The localized loan product description (business product name) | [optional] 
**loan_amount** | **str** | Total amount of the loan / principal | [optional] 
**maturity_date** | **date** | Loan maturity date | [optional] 
**principal_balance** | **str** | The amount outstanding that needs to be repaid to satisfy the debt | [optional] 
**scheduled_instalment_amount** | **str** | The next scheduled instalment amount | [optional] 
**scheduled_instalment_date** | **date** | The next scheduled instalment due date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


