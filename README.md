# smooth-visualization-of-delayed-satellite-imagery-main
AI-based Frame interpolation ,video generation and display system for wms

how to run the files

\\ cmd backend
   cd smooth-visualization-of-delayed-satellite-imagery-main
   python -m venv venv
   venv\Scripts\activate
   cd server
   pip install -r requirements.txt
   python .\app.py

   \\ cmd frontend
     cd frontend/server-processing
     python -m http.server

    \\ server number
    127.0.0:8000
