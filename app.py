import streamlit as st

# Configuração para remover margens e focar na placa
st.set_page_config(layout="wide", page_title="Gemini Pro DJ Unibody")

# --- O CÓDIGO DO HARDWARE SUPREMO ---
st.markdown("""
<style>
    /* Fundo de estúdio escuro */
    .stApp {
        background-color: #080808;
    }

    /* A PLACA ÚNICA (UNIBODY CHASSIS) */
    .dj-unibody {
        background: linear-gradient(145deg, #1e1e21 0%, #111113 100%);
        border: 2px solid #2a2a2e;
        border-radius: 20px;
        box-shadow: 
            0 30px 60px rgba(0,0,0,0.8),
            inset 0 1px 1px rgba(255,255,255,0.05);
        padding: 25px;
        margin: 10px auto;
        display: flex;
        flex-direction: row;
        gap: 15px;
        width: 98%;
        height: 85vh;
        position: relative;
    }

    /* Efeito de Metal Escovado Integrado */
    .dj-unibody::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(45deg, rgba(255,255,255,0.01) 0px, rgba(255,255,255,0.01) 1px, transparent 1px, transparent 2px);
        pointer-events: none;
        border-radius: 20px;
    }

    /* SEÇÃO DO BROWSER (Esquerda) */
    .embedded-sidebar {
        width: 260px;
        background: rgba(0,0,0,0.3);
        border-radius: 12px;
        border: 1px solid #222;
        padding: 15px;
        display: flex;
        flex-direction: column;
        box-shadow: inset 0 0 15px #000;
    }

    /* ÁREA DE CONTROLO COMPACTA (Centro e Direita) */
    .control-surface {
        flex-grow: 1;
        display: grid;
        grid-template-columns: 1fr 160px 1fr; /* Proporção ideal da placa real */
        gap: 10px;
        align-items: center;
    }

    /* JOG WHEELS COMPACTOS (Discos de Vinil) */
    @keyframes spin_record { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .deck-module {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .jog-vinyl {
        width: 320px;
        height: 320px;
        border-radius: 50%;
        background: radial-gradient(circle, #222 10%, #050505 100%);
        border: 12px solid #1a1a1c;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8), inset 0 0 10px #000;
        position: relative;
        animation: spin_record 4s linear infinite;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Ranhuras do Vinil */
    .jog-vinyl::after {
        content: "";
        position: absolute;
        width: 100%; height: 100%;
        border-radius: 50%;
        background: repeating-radial-gradient(circle, transparent 0, transparent 1px, rgba(255,255,255,0.02) 2px);
    }

    .jog-led-center {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: #000;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 20px #00f2ff66;
    }

    /* MIXER INTEGRADO (Central) */
    .center-mixer {
        background: rgba(0,0,0,0.4);
        border: 1px solid #2a2a2e;
        border-radius: 8px;
        height: 95%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px 5px;
        justify-content: space-around;
        box-shadow: inset 0 0 20px #000;
    }

    /* Ecrã LCD no topo da placa */
    .pro-display {
        background: #000;
        border: 1px solid #333;
        border-radius: 6px;
        color: #00f2ff;
        font-family: 'Courier New', monospace;
        padding: 5px 15px;
        margin-bottom: 10px;
        width: 200px;
        text-align: center;
        font-size: 13px;
        box-shadow: inset 0 0 5px #00f2ff33;
    }

    /* Estilização de Sliders para parecerem Faders de Mesa */
    .stSlider div[data-baseweb="slider"] {
        margin-top: -15px;
    }
    
    /* Botões LED Circulares */
    .stButton>button {
        border-radius: 50% !important;
        width: 60px !important;
        height: 60px !important;
        background: #222 !important;
        border: 2px solid #333 !important;
        color: #00f2ff !important;
        font-size: 10px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CONSTRUÇÃO DA PLACA ---

# Início da Placa de Metal Única
st.markdown('<div class="dj-unibody">', unsafe_allow_html=True)

# 1. BROWSER SOUNDCLOUD INTEGRADO (Esquerda)
with st.container():
    st.markdown('<div class="embedded-sidebar">', unsafe_allow_html=True)
    st.markdown("### ☁️ SOUNDCLOUD")
    st.text_input("Search", placeholder="Track, Artist...", label_visibility="collapsed")
    st.markdown("---")
    st.caption("EXPLORE")
    st.write("🔥 Trending")
    st.write("🎹 Techno")
    st.write("🎧 Deep House")
    st.write("🌑 Dark Ambient")
    st.markdown("<br>"*5, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("MASTER GAIN")
    st.slider("", 0, 100, 80, key="mst")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. SUPERFÍCIE DE CONTROLO (Decks + Mixer)
st.markdown('<div class="control-surface">', unsafe_allow_html=True)

# --- DECK A (Esquerdo) ---
st.markdown('<div class="deck-module">', unsafe_allow_html=True)
st.markdown('<div class="pro-display">DECK A | 128.0 BPM<br>04:20 / 06:15</div>', unsafe_allow_html=True)
st.markdown('<div class="jog-vinyl"><div class="jog-led-center"></div></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.button("PLAY", key="a_p")
c2.button("CUE", key="a_c")
c3.button("SYNC", key="a_s")
st.slider("Pitch A", -10.0, 10.0, 0.0, key="pitch_a")
st.markdown('</div>', unsafe_allow_html=True)

# --- MIXER CENTRAL ---
st.markdown('<div class="center-mixer">', unsafe_allow_html=True)
st.caption("GAIN")
st.slider("G1", 0, 100, 75, key="g1", label_visibility="collapsed")
st.markdown("---")
st.caption("HI")
st.slider("H1", 0, 100, 50, key="h1", label_visibility="collapsed")
st.caption("MID")
st.slider("M1", 0, 100, 50, key="m1", label_visibility="collapsed")
st.caption("LOW")
st.slider("L1", 0, 100, 50, key="l1", label_visibility="collapsed")
st.markdown("---")
st.caption("CROSSFADER")
st.slider("XF", -100, 100, 0, key="xf", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# --- DECK B (Direito) ---
st.markdown('<div class="deck-module">', unsafe_allow_html=True)
st.markdown('<div class="pro-display" style="color:#ff2d55; border-color:#ff2d5544;">DECK B | 128.0 BPM<br>02:10 / 05:45</div>', unsafe_allow_html=True)
st.markdown('<div class="jog-vinyl" style="animation-duration: 3s;"><div class="jog-led-center" style="border-color:#ff2d55; box-shadow: 0 0 20px #ff2d5566;"></div></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
c4, c5, c6 = st.columns(3)
c4.button("PLAY", key="b_p")
c5.button("CUE", key="b_c")
c6.button("SYNC", key="b_s")
st.slider("Pitch B", -10.0, 10.0, 0.0, key="pitch_b")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fim da Control Surface

st.markdown('</div>', unsafe_allow_html=True) # Fim do Unibody Chassis
