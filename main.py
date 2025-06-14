from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse

# Explicit router imports
from app.api.solve import router as solve_router
from app.api.explain import router as explain_router
from app.api.trace import router as trace_router
from app.api.debug import router as debug_router
from app.api.translate import router as translate_router
from app.api.solve_legacy import router as solve_legacy_router
from app.api.quantum import router as quantum_router
from app.api.scroll import router as scroll_router
from app.api.schema import router as schema_router

app = FastAPI(
    title="Evo33: Codex Reasoning Engine",
    description="Symbolic logic evaluation, paradox detection, digital provenance, and natural language reasoning.",
    version="1.0.0"
)

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Plugin/landing routes
@app.get("/openapi.yaml")
def get_openapi():
    return FileResponse("static/openapi.yaml", media_type="text/yaml")

@app.get("/.well-known/ai-plugin.json")
def get_manifest():
    return FileResponse("static/.well-known/ai-plugin.json", media_type="application/json")

@app.get("/robots.txt")
def get_robots():
    return FileResponse("static/robots.txt", media_type="text/plain")

@app.get("/", response_class=HTMLResponse)
def serve_index():
    return FileResponse("static/index.html")

  # New explicit routes for Privacy, Legal, User Rights
@app.get("/privacy", response_class=HTMLResponse)
def privacy():
    return FileResponse("static/privacy.html")

@app.get("/legal", response_class=HTMLResponse)
def legal():
    return FileResponse("static/legal.html")

@app.get("/user-rights", response_class=HTMLResponse)
def user_rights():
    return FileResponse("static/user-rights.html")  

# Include API routers explicitly
app.include_router(solve_router, prefix="/solve", tags=["Logic Solving"])
app.include_router(explain_router, prefix="/explain", tags=["Explanation Engine"])
app.include_router(trace_router, prefix="/trace", tags=["Proof Tracing"])
app.include_router(debug_router, prefix="/debug", tags=["Debugging"])
app.include_router(translate_router, prefix="/translate", tags=["Translation Engine"])
app.include_router(solve_legacy_router, prefix="/solve-legacy", tags=["Legacy Logic"])
app.include_router(quantum_router, prefix="/quantum", tags=["Quantum Mode"])
app.include_router(scroll_router, prefix="/scroll", tags=["Codex Reasoning"])
app.include_router(schema_router, prefix="/schema", tags=["Schema Explorer"])
