from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

router = APIRouter(prefix='/accounts_pay_receive')


class AccountsPayReceiveResponse(BaseModel):
    id: int
    description: str
    value: Decimal
    type: str #pagar,receber

class AccountPayReceiveRequest(BaseModel)    :
    description: str
    value: Decimal
    type: str #pagar,receber

@router.get('/', response_model=List[AccountsPayReceiveResponse])
def list_accounts():
    return [
        AccountsPayReceiveResponse(
            id=1,
            description='Conta1',
            value=1600,
            type='PAGAR'
        ),
        AccountsPayReceiveResponse(
            id=1,
            description='Salário',
            value=1000,
            type='RECEBER'
        ),
    ]

@router.post('/', response_model=AccountsPayReceiveResponse, status_code=201)
def create_account(account: AccountPayReceiveRequest):
    return AccountsPayReceiveResponse(
        id=3,
        description=account.description,
        value=account.value,
        type=account.type
    )
