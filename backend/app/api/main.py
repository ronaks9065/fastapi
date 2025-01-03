# mypy: disable-error-code="attr-defined"
# Third-party imports
from fastapi import APIRouter
from app.api.routes.assets import router as asset_router
from app.api.routes.policies import router as policy_router
from app.api.routes.contract_agreement import router as agreement_router
from app.api.routes.contract_negotiations import router as negotiation_router
from app.api.routes.contracts_definition import router as definition_router
from app.api.routes.data_offers import router as data_offer_router
from app.api.routes.data_transfers import router as data_transfer_router
from app.api.routes.edc import router as edc_router

# Local application imports
from app.api.routes import auth, items, login, users, utils


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(asset_router, prefix="/assets", tags=["Assets"])
api_router.include_router(policy_router, prefix="/policies", tags=["Policies"])
api_router.include_router(
    agreement_router, prefix="/agreements", tags=["Contract Agreements"]
)
api_router.include_router(
    negotiation_router, prefix="/negotiations", tags=["Contract Negotiations"]
)
api_router.include_router(
    definition_router, prefix="/definitions", tags=["Contract Definitions"]
)
api_router.include_router(
    data_offer_router, prefix="/data-offers", tags=["Data Offers"]
)
api_router.include_router(
    data_transfer_router, prefix="/data-transfers", tags=["Data Transfers"]
)
api_router.include_router(edc_router, prefix="/edc", tags=["EDC"])
api_router.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
