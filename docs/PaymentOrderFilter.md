# PaymentOrderFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The payment order state | [optional] 
**type** | **str** | The payment order type | [optional] 
**partner_account** | [**PaymentOrderFilterPartnerAccount**](PaymentOrderFilterPartnerAccount.md) |  | [optional] 
**amount_from** | **str** | The minimal payment amount for filtering | [optional] 
**amount_to** | **str** | The maximal payment amount for filtering | [optional] 
**date_from** | **date** | The minimal effective/value date for filtering | [optional] 
**date_to** | **date** | The maximal effective/value date for filtering | [optional] 
**variable_symbol** | **str** | The variable symbol (exact match) | [optional] 
**bulk_payment_order_id** | **str** | The unique identifier for bulk order the payment is associated with | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


