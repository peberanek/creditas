# PaymentOrderForeign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_order_id** | **str** | The unique identifier for the payment order | [optional] 
**state** | **str** | The payment order state | [optional] 
**type** | **str** | The payment order type | [optional] 
**source_account** | [**SourceAccount**](SourceAccount.md) |  | [optional] 
**partner_account** | [**PaymentOrderForeignPartnerAccount**](PaymentOrderForeignPartnerAccount.md) |  | [optional] 
**amount** | [**Money**](Money.md) |  | [optional] 
**amount_in_account_currency** | [**Money**](Money.md) |  | [optional] 
**exchange_rate** | **str** | The conversion exchange rate when the transfer currency differs from the account currency | [optional] 
**payment_title** | **str** | The payment classification code according to CNB | [optional] 
**fee_instruction** | **str** | The fee sharing instruction code - SHA, BEN, OUR | [optional] 
**remittance_info** | **str** | The remittance information - additional information for the payment beneficiary | [optional] 
**user_note** | **str** | The user defined note (it is not sent to beneficiary‘s bank) | [optional] 
**due_date** | **date** | The payment order due date | [optional] 
**created** | **datetime** | The date and time the payment order has been created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


