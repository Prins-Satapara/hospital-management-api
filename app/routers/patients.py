from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from typing import Literal
from app.models.patient import Patient, PatientUpdate
from app.services.data import load_data, save_data

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)



@router.get("/", summary="Get all patients")
def get_all_patients(): 
    data = load_data()
    return data


@router.get("/sort", summary="Sort Patients")
def sort_patient(
    sort_by: Literal["height", "weight", "bmi"] = Query(
        ..., 
        description="Sort patients by height, weight or BMI"
    ),
    order: Literal["asc", "desc"] = Query('asc', description='Sort Order')
):
        
    data = load_data()
    reverse_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse= reverse_order)
    return sorted_data


@router.post("/", summary="Create Patient")
def create_patient(patient: Patient):
    
    data = load_data()
    
    # check if patient is already exists
    if patient.id in data:
        raise HTTPException(
            status_code=400, 
            detail=f"patient with id {patient.id} is already exist"
        )
    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude={'id'})
    
    # save the data
    save_data(data) 

    return JSONResponse(
        status_code=201, 
        content= {"message": f"patient with id {patient.id} created successfully."}
    )


@router.get("/{patient_id}", summary="Get patient by ID")
def get_patient(patient_id: str = Path(..., description="ID of the patient in the DB", examples=['P001'])):
    #load the entire data
    data = load_data()
    
    # check that patient is exist in data or not
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )


@router.put("/{patient_id}", summary="Update Patient")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(
            status_code=404, 
            detail="Patient not found!"
        )
        
    existing_patient_info = data[patient_id]
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
    
    # add id in dict
    existing_patient_info['id'] = patient_id
    # create pydantic obj
    patient_pydantic_obj = Patient(**existing_patient_info)
    # remove id from dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude={'id'})
    
    # add this dict into data
    data[patient_id] = existing_patient_info
    
    # save data 
    save_data(data)
    
    return JSONResponse(
        status_code=200,
        content= {"message": f"Patient with id {patient_id} updated successfully.."}
    )
    

@router.delete("/{patient_id}", summary="Delete Patient")
def delete_patient(patient_id: str):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(
            status_code=404, 
            detail="Patient not found"
        )
    
    del data[patient_id]
    
    save_data(data)
    
    return JSONResponse(
        status_code=200, 
        content={
            "message": f"patient with id {patient_id} is successfully deleted..."
        }
    )