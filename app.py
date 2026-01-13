import streamlit as st

# Configuração de ecrã inteiro
st.set_page_config(layout="wide", page_title="Professional DJ Station")

# --- CSS DE ALTA FIDELIDADE (O Visual da Imagem) ---
st.markdown("""
<style>
    /* Estética de Fundo */
    .stApp {
        background-color: #121214;
    }

    /* Estrutura Principal */
    .dj-system {
        display: grid;
        grid-template-columns: 250px 1fr 250px;
        gap: 20px;
        padding: 20px;
        height: 90vh;
    }

    /* Navegadores Laterais (SoundCloud Style) */
    .nav-panel {
        background: #1c1c1f;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #2d2d32;
        color: #8e8e93;
    }

    /* A MESA DE DJ (O Retângulo Preto da Imagem) */
    .dj-chassis {
        background: linear-gradient(180deg, #1e1e21 0%, #161618 100%);
        border-radius: 24px;
        border: 2px solid #3a3a3e;
        box-shadow: 0 40px 80px rgba(0,0,0,0.9);
        padding: 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
    }

    /* Discos de Vinil (Jog Wheels) */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-wheel {
        width: 320px;
        height: 320px;
        border-radius: 50%;
        background: radial-gradient(circle, #2c2c30 0%, #000 70%);
        border: 12px solid #28282b;
        box-shadow: 0 0 20px rgba(0,0,0,0.5), inset 0 0 15px #000;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        animation: spin 3s linear infinite;
    }

    .jog-wheel::before {
        content: "";
        position: absolute;
        width: 100%; height: 100%;
        border-radius: 50%;
        background: repeating-radial-gradient(circle, transparent 0, transparent 1px, rgba(255,255,255,0.02) 2px);
    }

    .jog-center-led {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: #000;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 15px #00f2ff66;
    }

    /* Mixer Central (A parte dos botões no meio) */
    .mixer-unit {
        width: 240px;
        height: 100%;
        background: rgba(0,0,0,0.2);
        border-left: 2px solid #2d2d32;
        border-right: 2px solid #2d2d32;
        padding: 0 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    }

    /* Ecrãs LCD */
    .lcd-screen {
        background: #000;
        border: 1px solid #333;
        color: #00f2ff;
        font-family: 'monospace';
        padding: 8px;
        width: 120px;
        text-align: center;
        font-size: 12px;
        border-radius: 4px;
        margin-bottom: 10px;
        box-shadow: inset 0 0 5px #00f2ff33;
    }

    /* Botões Iluminados */
    .stButton>button {
        border-radius: 8px !important;
        background: #252529 !important;
        border: 1px solid #3a3a3e !important;
        color: white !important;
        font-weight: bold !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        border-color: #00f2ff !important;
        box-shadow: 0 0 10px #00f2ff66 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CONSTRUÇÃO DO INTERFACE ---

st.markdown('<div class="dj-system">', unsafe_allow_html=True)

# 1. Navegador Esquerdo (SoundCloud)
with st.container():
    st.markdown('<div class="nav-panel">', unsafe_allow_html=True)
    st.title("☁️")
    st.markdown("### SoundCloud")
    st.markdown("---")
    st.write("🎵 My Tracks")
    st.write("🔥 Trending")
    st.write("🎧 Playlists")
    st.markdown("<br>"*10, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. Mesa Central (O Retângulo Preto)
with st.container():
    st.markdown('<div class="dj-chassis">', unsafe_allow_html=True)
    
    # DECK ESQUERDO
    with st.container():
        st.markdown('<div class="lcd-screen">124.0 BPM<br>DECK A</div>', unsafe_allow_html=True)
        st.markdown('<div class="jog-wheel"><div class="jog-center-led"></div></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.button("PLAY", key="play_a")
        col2.button("SYNC", key="sync_a")
        st.slider("Pitch A", -8.0, 8.0, 0.0, key="p_a")

    # MIXER CENTRAL
    st.markdown('<div class="mixer-unit">', unsafe_allow_html=True)
    st.write("LEVEL")
    st.slider("Master", 0, 100, 70, label_visibility="collapsed")
    st.write("EQ")
    st.slider("HI", 0, 100, 50, label_visibility="collapsed", key="hi")
    st.slider("MID", 0, 100, 50, label_visibility="collapsed", key="mid")
    st.slider("LOW", 0, 100, 50, label_visibility="collapsed", key="low")
    st.write("CROSSFADER")
    st.slider("CF", -100, 100, 0, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # DECK DIREITO
    with st.container():
        st.markdown('<div class="lcd-screen" style="color:#ff2d55; border-color:#ff2d5533;">124.0 BPM<br>DECK B</div>', unsafe_allow_html=True)
        st.markdown('<div class="jog-wheel" style="animation-duration: 2.5s;"><div class="jog-center-led" style="border-color:#ff2d55; box-shadow: 0 0 15px #ff2d5566;"></div></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        col3.button("PLAY", key="play_b")
        col4.button("SYNC", key="sync_b")
        st.slider("Pitch B", -8.0, 8.0, 0.0, key="p_b")

    st.markdown('</div>', unsafe_allow_html=True) # Fim do Chassis

# 3. Navegador Direito (SoundCloud Search)
with st.container():
    st.markdown('<div class="nav-panel">', unsafe_allow_html=True)
    st.markdown("### 🔍 Search")
    query = st.text_input("SoundCloud Music", placeholder="Artist, song...")
    st.markdown("---")
    st.caption("Results:")
    if query:
        st.write(f"🎧 {query} - Remix")
        st.write(f"🎧 {query} - Original")
    else:
        st.write("1. Peggy Gou - Nanana")
        st.write("2. Mau P - Drugs From Amsterdam")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
