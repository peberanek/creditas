# AccountTransactionFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The transaction category | [optional] 
**type** | **str** | The transaction type | [optional] 
**partner_account** | [**AccountTransactionFilterPartnerAccount**](AccountTransactionFilterPartnerAccount.md) |  | [optional] 
**amount_from** | **str** | The minimal transaction amount for filtering | [optional] 
**amount_to** | **str** | The maximal transaction amount for filtering | [optional] 
**date_from** | **date** | The minimal effective/value date for filtering | [optional] 
**date_to** | **date** | The maximal effective/value date for filtering | [optional] 
**variable_symbol** | **str** | The variable symbol (exact match) | [optional] 
**specific_symbol** | **str** | The specific symbol (exact match) | [optional] 
**constant_symbol** | **str** | The constant symbol (exact match) | [optional] 
**payers_reference** | **str** | Information allowing the beneficiary to identify the payment | [optional] 
**remittance_info** | **str** | The remittance information - additional information for the payment beneficiary | [optional] 
**payment_order_id** | **str** | The unique identifier for the payment order the transaction is associated with | [optional] 
**bulk_payment_order_id** | **str** | The unique identifier for the bulk payment order the transaction is associated with | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


