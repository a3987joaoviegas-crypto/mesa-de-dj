import streamlit as st
import streamlit.components.v1 as components

# 1. Configuração inicial (Tem de ser a primeira coisa!)
st.set_page_config(page_title="DJ MASTER MIXER", layout="wide")

# 2. Proteção contra o AttributeError (Define as cores antes de tudo)
if 'neon_color' not in st.session_state:
    st.session_state.neon_color = "#00FF00"
if 'pA' not in st.session_state: st.session_state.pA = False
if 'pB' not in st.session_state: st.session_state.pB = False

# 3. Estilo Visual (Luzes e Design)
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: {st.session_state.neon_color}; }}
    .plate {{
        width: 200px; height: 200px; border-radius: 50%;
        background: radial-gradient(circle, #333 10%, #000 90%);
        border: 5px solid {st.session_state.neon_color};
        margin: auto; box-shadow: 0 0 20px {st.session_state.neon_color};
    }}
    .playing {{ animation: rotate 2s linear infinite; }}
    @keyframes rotate {{ from {{transform: rotate(0deg);}} to {{transform: rotate(360deg);}} }}
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 DJ NEON STUDIO PRO")

# 4. Mesa de Mistura
col1, col2, col3 = st.columns([2,1,2])

with col1:
    st.subheader("DECK A")
    cl_a = "plate playing" if st.session_state.pA else "plate"
    st.markdown(f'<div class="{cl_a}"></div>', unsafe_allow_html=True)
    if st.button("PLAY/PAUSE A"): st.session_state.pA = not st.session_state.pA

with col2:
    st.write("🎚️ MIXER")
    st.slider("CROSSFADER", -100, 100, 0)
    if st.button("⚡ AIRHORN"): st.toast("📢 BEEP!")

with col3:
    st.subheader("DECK B")
    cl_b = "plate playing" if st.session_state.pB else "plate"
    st.markdown(f'<div class="{cl_b}"></div>', unsafe_allow_html=True)
    if st.button("PLAY/PAUSE B"): st.session_state.pB = not st.session_state.pB

# 5. Spotify e Instrumentos
st.divider()
t1, t2 = st.tabs(["🎵 SPOTIFY", "🎹 INSTRUMENTOS"])

with t1:
    url = st.text_input("Cola o link da música:", "https://open.spotify.com/track/4PTG3u69goa97S9vY7S9X0")
    if "track/" in url:
        id_m = url.split("track/")[1].split("?")[0]
        st.markdown(f'<iframe src="https://open.spotify.com/embed/track/{id_m}" width="100%" height="352" frameborder="0" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

with t2:
    c_i = st.columns(4)
    insts = ["🎹 Piano", "🎸 Guitarra", "🥁 Bateria", "🎷 Sax"]
    for i, inst in enumerate(insts):
        if c_i[i].button(inst): st.success(f"A tocar {inst}...")

# 6. Sidebar
st.sidebar.title("Configurações")
st.session_state.neon_color = st.sidebar.color_picker("Cor do Sistema", "#00FF00")
