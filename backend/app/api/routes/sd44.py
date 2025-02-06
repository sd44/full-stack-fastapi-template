from fastapi import APIRouter

router = APIRouter(tags=["sd44"])


# 不完善，没有定义pydantic返回类型
@router.get("/sd44/")
def read_items() -> list[dict[str, str]]:
    return [{"name": "Empanada"}, {"name": "Arepa"}]
