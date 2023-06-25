# DebitCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | The unique identifier for the card | [optional] 
**number** | **str** | The card number masked | [optional] 
**currency** | **str** | The card&#39;s currency code in ISO 4217 format (CZK, EUR, USD, ...) | [optional] 
**status** | **str** | The status of the card (ACTIVE, INACTIVE, BLOCKED, CLOSED, TO_BE_CLOSED) | [optional] 
**holder** | **str** | Name of the card holder | [optional] 
**alias** | **str** | The consumer preferred card name | [optional] 
**product_i18_n** | **str** | The localized bank card product description (business product name) | [optional] 
**available_balance** | **str** | The available balance for the card (may include pending transactions and overdraft limit) | [optional] 
**brand** | **str** | The card brand (VISA, MASTER, MAESTRO, ...) | [optional] 
**expiration** | **date** | The expiration date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


