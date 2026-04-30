"""FastAPI entry point for Budget Copilot application"""

# Importing service modules to ensure they are registered
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Initialize FastAPI app
app = FastAPI(
    title="Budget Copilot",
    description="Intelligent budget management and expense tracking API",
    version="1.0.0"
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running
       Returns a simple JSON response indicating the API is healthy"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "app": "Budget Copilot",
            "version": "1.0.0"
        }
    )

# Root endpoint
@app.get("/")
async def read_root():
    """Root endpoint providing basic information about the API
       Returns a welcome message and a brief description 
       of the API's functionality"""
    
    return {
        "message": "Welcome to Budget Copilot API",
        "description": "Intelligent budget management and expense tracking API"
        }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
