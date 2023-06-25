# Body18

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account** | [**PaymentsepacreateSourceAccount**](PaymentsepacreateSourceAccount.md) |  | [optional] 
**partner_account** | [**PaymentforeigncreatePartnerAccount**](PaymentforeigncreatePartnerAccount.md) |  | [optional] 
**amount** | [**Money**](Money.md) |  | [optional] 
**payment_title** | **str** | The payment classification code according to CNB | [optional] 
**fee_instruction** | **str** | The fee sharing instruction code - SHA, BEN, OUR | 
**remittance_info** | **str** | The remittance information - additional information for the payment beneficiary | 
**user_note** | **str** | The user defined note (it is not sent to beneficiary‘s bank) | [optional] 
**due_date** | **date** | The payment order due date | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


