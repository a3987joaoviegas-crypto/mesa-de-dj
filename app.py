import streamlit as st

# Configuração Pro
st.set_page_config(page_title="FL Streamlit Studio", layout="wide")

# --- CSS DE ALTO REALISMO (ESTILO DAW) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');
    
    .stApp { background-color: #1e1e1e; color: #dcdcdc; font-family: 'Roboto Mono', monospace; }
    
    /* Botões estilo FL Studio */
    .stButton>button {
        background: linear-gradient(145deg, #333, #222);
        border: 1px solid #444;
        color: #ff9000;
        font-weight: bold;
        border-radius: 4px;
        box-shadow: 2px 2px 5px #111;
        height: 40px;
    }
    .stButton>button:active { background: #ff9000; color: black; }
    
    /* Painéis de Rack */
    .rack-panel {
        background-color: #2b2b2b;
        border-left: 5px solid #ff9000;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    /* Medidores de LED */
    .vu-meter {
        height: 10px;
        background: linear-gradient(to right, green 60%, yellow 80%, red 100%);
        border-radius: 2px;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO DA DAW ---
col_logo, col_transport, col_cpu = st.columns([1, 2, 1])
with col_logo:
    st.markdown("<h2 style='color: #ff9000; margin:0;'>FL STUDIO <span style='font-size:12px; color:white;'>ST</span></h2>", unsafe_allow_html=True)
with col_transport:
    c1, c2, c3, c4 = st.columns(4)
    c1.button("▶ PLAY")
    c2.button("⏸ PAUSE")
    c3.button("⏹ STOP")
    c4.button("🔴 REC")

st.divider()

# --- ÁREA PRINCIPAL: STEP SEQUENCER & PLAYLIST ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 🎛 CHANNEL RACK (Step Sequencer)")
    
    instruments = ["🥁 KICK", "💥 SNARE", "✨ HI-HAT", "🎸 BASS"]
    for inst in instruments:
        with st.container():
            cols = st.columns([2, 8])
            cols[0].write(f"**{inst}**")
            # Simulação de passos (steps) do sequenciador
            steps = cols[1].columns(8)
            for i in range(8):
                steps[i].checkbox("", key=f"{inst}_{i}")
            st.markdown("<div class='vu-meter'></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎹 PIANO ROLL / SPOTIFY SELECTOR")
    spotify_url = st.text_input("Drop Spotify Track URL here:", "https://open.spotify.com/track/4cOdK2wGvWyRJBUNRJVY0q")
    if "track/" in spotify_url:
        track_id = spotify_url.split("track/")[1].split("?")[0]
        st.markdown(f'<iframe src="https://open.spotify.com/embed/track/{track_id}" width="100%" height="152" frameborder="0" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

with col_right:
    st.markdown("### 🎚️ MIXER")
    st.markdown("<div style='background:#111; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.slider("INS 1", 0, 100, 80, label_visibility="collapsed")
        st.caption("MASTER")
    with m_col2:
        st.slider("INS 2", 0, 100, 50, label_visibility="collapsed")
        st.caption("TRACK 1")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 📦 EFFECTS SLOT")
    st.selectbox("Slot 1", ["None", "Fruity Reverb 2", "Fruity Limiter", "Gross Beat"])
    st.selectbox("Slot 2", ["None", "Fruity Delay 3", "Soundgoodizer"])
    
    st.divider()
    st.markdown("### 🕒 BROWSER")
    st.caption("📁 Packs")
    st.caption("📁 Project Bones")
    st.caption("📁 Recorded")

# --- RODAPÉ INFO ---
st.sidebar.image("https://www.image-line.com/wp-content/uploads/2020/03/flstudio_logo_dark.png", width=100)
st.sidebar.title("PROJECT INFO")
st.sidebar.number_input("BPM", 10, 250, 128)
st.sidebar.selectbox("Time Sig", ["4/4", "3/4", "6/8"])
st.sidebar.slider("CPU Load", 0, 100, 12)
