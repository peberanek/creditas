# AccountTermDeposit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique identifier for the account | [optional] 
**bban** | **str** | BBAN (Basic Bank Account Number) The country-specific account number | [optional] 
**bank_code** | **str** | The country-specific bank code | [optional] 
**iban** | **str** | IBAN (International Bank Account Number) | [optional] 
**bic** | **str** | BIC (Business Identification Code) - International unique identifier for the bank | [optional] 
**currency** | **str** | The account&#39;s currency code in ISO 4217 format (CZK, EUR, USD, ...) | [optional] 
**country** | **str** | The country code of the account&#39;s origin in ISO 3166-1 alpha-3 format (CZE, SVK, ...) | [optional] 
**status** | **str** | The status of the account (ACTIVE, INACTIVE, CLOSED, TO_BE_CLOSED) | [optional] 
**name** | **str** | The name (description) for the account (typically the name of the account&#39;s owner) | [optional] 
**alias** | **str** | The consumer preferred account name | [optional] 
**product_i18_n** | **str** | The localized bank account product description (business product name) | [optional] 
**balance** | **str** | The total account value | [optional] 
**term_deposit_amount** | **str** | The original amount of the term deposit invested at the beginning of its term | [optional] 
**maturity_date** | **date** | The date at which the term deposit reaches the last date of its term | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


