import fastapi
import fastapi.security as security
import schemas
import services
import sqlalchemy.orm as orm

app = fastapi.FastAPI()


@app.post("/api/users", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, db: orm.Session = fastapi.Depends(services.get_db)
):
    db_user = await services.get_user_by_email(user.email, db)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email already in use.")

    return await services.create_user(user, db)
