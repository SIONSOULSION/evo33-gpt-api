from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

@app.get("/", response_class=HTMLResponse)
def serve_index():
    return FileResponse("static/index.html")

from app.api import solve, explain, trace, debug, translate
from app.api import solve_legacy, quantum, scroll, schema

app = FastAPI(
    title="Evo33: Codex Reasoning Engine",
    description="Symbolic logic evaluation, paradox detection, digital provenance, and natural language reasoning.",
    version="1.0.0"
)

# CORS
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
def serve_markdown():
    try:
        with open("static/index.md", "r", encoding="utf-8") as f:
            md_content = f.read()
        html = markdown.markdown(md_content)
        return f"""
        <html>
          <head>
            <title>Evo 33 – Codex Reasoning Engine</title>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
            <meta property='og:title' content='Evo 33 – Codex Reasoning Engine'>
            <meta property='og:description' content='Symbolic logic evaluation, paradox detection, and digital provenance – now available as a GPT.'>
            <meta property='og:image' content='https://evo33.io/logo.png'>
            <meta property='og:url' content='https://evo33.io'>
          </head>
          <body style='font-family:sans-serif; max-width:700px; margin:auto; padding:2em;'>
            {html}
          </body>
        </html>
        """
    except:
        return HTMLResponse(content="<h1>Welcome to Evo 33</h1><p>Static landing page not found.</p>", status_code=200)

# Include core and new modules
app.include_router(solve.router, prefix="/solve", tags=["Logic Solving"])
app.include_router(explain.router, prefix="/explain", tags=["Explanation Engine"])
app.include_router(trace.router, prefix="/trace", tags=["Proof Tracing"])
app.include_router(debug.router, prefix="/debug", tags=["Debugging"])
app.include_router(translate.router, prefix="/translate", tags=["Translation Engine"])
app.include_router(solve_legacy, prefix="/solve-legacy", tags=["Legacy Logic"])
app.include_router(quantum, prefix="/quantum", tags=["Quantum Mode"])
app.include_router(scroll, prefix="/scroll", tags=["Codex Reasoning"])
app.include_router(schema, prefix="/schema", tags=["Schema Explorer"])