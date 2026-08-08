from fastapi import FastAPI

from app.services.data import load_data, save_data
from app.models.patient import Patient, PatientUpdate
from app.routers.patients import router as patient_router

app = FastAPI(
    title='Hospital Management API',
    description="Rest API for managing patient records",
    version="1.0.0"
)

@app.get("/")
def hello():
    return{"massage": "Patient Management System API"}

@app.get("/about")
def about():
    return{"massage": "A fully functional API to manage your patient records"}


app.include_router(patient_router)