# AccountTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier for the transaction record | 
**category** | **str** | The transaction category | 
**type** | **str** | The transaction type | 
**code** | **str** | The transaction code | 
**code_i18_n** | **str** | The transaction code localized description | [optional] 
**partner_account** | [**AccountTransactionPartnerAccount**](AccountTransactionPartnerAccount.md) |  | [optional] 
**amount** | [**Money**](Money.md) |  | 
**effective_date** | **date** | The transaction effective/value date | 
**card_authorization_date** | **date** | The date of the card transaction authorization | [optional] 
**variable_symbol** | **str** | The variable symbol | [optional] 
**specific_symbol** | **str** | The specific symbol | [optional] 
**constant_symbol** | **str** | The constant symbol | [optional] 
**payers_reference** | **str** | Information allowing the beneficiary to identify the payment | [optional] 
**remittance_info** | **str** | The remittance information - additional information for the payment beneficiary | [optional] 
**user_note** | **str** | The user defined note | [optional] 
**balance** | [**Money**](Money.md) |  | [optional] 
**payment_order_id** | **str** | The unique identifier for the payment order the transaction is associated with | [optional] 
**bulk_payment_order_id** | **str** | The unique identifier for the bulk payment order the transaction is associated with | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


