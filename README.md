# Chanakya Computer Institute — Streamlit

This package wraps the existing `index.html` app in Streamlit so it can be deployed on Streamlit Community Cloud.

## Files
- `app.py` — Streamlit launcher
- `index.html` — your original app
- `requirements.txt` — Streamlit dependency

## Deploy
1. Upload these files to a GitHub repository.
2. Open Streamlit Community Cloud.
3. Create a new app.
4. Select the GitHub repository.
5. Set the main file to `app.py`.
6. Deploy.

Important: the current HTML app stores its data in browser `localStorage`. Running it through Streamlit does not automatically create a cloud database or shared database.
