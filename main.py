from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# -----------------------------
# Import Routers
# -----------------------------
from backend.api.project_routes import router as project_router
from backend.api.testcase_routes import router as testcase_router
from backend.api.playwright_routes import router as playwright_router
from backend.api.execution_routes import router as execution_router
from backend.api.report_routes import router as report_router
from backend.api.dashboard_routes import router as dashboard_router
from backend.api.auth_routes import router as auth_router

# -----------------------------
# Create FastAPI App
# -----------------------------
app = FastAPI(
    title="AI QA Engine",
    description="AI Powered Test Automation Engine",
    version="1.0.0",
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Static Files (Allure Reports)
# -----------------------------
app.mount(
    "/allure",
    StaticFiles(directory="reports"),
    name="allure",
)

# -----------------------------
# Register Routers
# -----------------------------
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(testcase_router)
app.include_router(playwright_router)
app.include_router(execution_router)
app.include_router(report_router)
app.include_router(dashboard_router)

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "AI QA Engine Backend is Running 🚀"
    }