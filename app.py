import streamlit as st, pytz
import streamlit.components.v1 as components
from datetime import datetime

# Set page config (optional)
# st.set_page_config(page_title="My Streamlit PWA", page_icon="icon-192x192.png")

st.subheader("Streamlit PWA Test", divider="rainbow")

india_tz = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(india_tz)
st.code(f'''
🌎 Country: India \n
📅 Current Day: {current_time.strftime("%d-%b-%Y")} \n
🕒 Current Time: {current_time.strftime("%H:%M:%S")}
''')

# Include the PWA manifest and service worker
components.html("""
<link rel="manifest" href="/manifest.json">
<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/service-worker.js')
    .then(function(registration) {
      console.log('Service Worker registered with scope:', registration.scope);
    })
    .catch(function(error) {
      console.log('Service Worker registration failed:', error);
    });
  }
</script>
""", height=0)
