import streamlit as st

# Configuração de ecrã inteiro sem margens
st.set_page_config(layout="wide", page_title="Unibody DJ Metal Station")

# --- O DESIGN DA PLACA DE METAL ÚNICA ---
st.markdown("""
<style>
    /* Fundo da "Sala de Estúdio" */
    .stApp {
        background-color: #0a0a0b;
    }

    /* A PLACA DE METAL (Hardware Único) */
    .metal-chassis {
        background: linear-gradient(135deg, #2c2c2e 0%, #1c1c1e 50%, #111112 100%);
        border: 3px solid #3a3a3c;
        border-radius: 20px;
        box-shadow: 0 50px 100px rgba(0,0,0,0.9), inset 0 2px 2px rgba(255,255,255,0.1);
        margin: 20px auto;
        padding: 30px;
        display: flex;
        gap: 20px;
        height: 85vh;
        width: 95%;
        position: relative;
    }

    /* Textura de Metal Escovado (Overlay) */
    .metal-chassis::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        opacity: 0.05;
        pointer-events: none;
        background-image: repeating-linear-gradient(45deg, #fff, #fff 1px, transparent 1px, transparent 2px);
    }

    /* Secção do Navegador Embutida no Metal */
    .embedded-browser {
        flex: 1;
        background: rgba(0, 0, 0, 0.4);
        border-radius: 12px;
        border: 1px solid #333;
        padding: 20px;
        overflow-y: auto;
        box-shadow: inset 0 0 20px #000;
    }

    /* A Secção da Mesa (Decks + Mixer) */
    .deck-area {
        flex: 3;
        display: grid;
        grid-template-columns: 1fr 180px 1fr;
        gap: 15px;
        align-items: center;
    }

    /* Discos (Jog Wheels) Ultra Realistas */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-wheel {
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: radial-gradient(circle, #222 20%, #000 100%);
        border: 8px solid #2a2a2d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8), inset 0 0 10px #000;
        margin: 20px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        animation: spin 3.5s linear infinite;
    }

    .jog-wheel::after {
        content: "";
        position: absolute;
        width: 100%; height: 100%;
        border-radius: 50%;
        background: repeating-radial-gradient(circle, transparent 0, transparent 1px, rgba(255,255,255,0.02) 2px);
    }

    .jog-center {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 15px #00f2ff;
        background: #111;
    }

    /* Ecrã de Informação */
    .digital-display {
        background: #000;
        color: #00f2ff;
        font-family: 'Courier New', Courier, monospace;
        border: 1px solid #333;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2);
    }

    /* Mixer Integrado */
    .integrated-mixer {
        background: rgba(0,0,0,0.3);
        border-radius: 8px;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px 0;
        border: 1px solid #3a3a3c;
    }

    /* Estilo dos Sliders e Botões */
    .stSlider label { color: #888 !important; font-size: 0.7em !important; }
    .stButton>button {
        background: #222 !important;
        border: 1px solid #444 !important;
        color: #ddd !important;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTEÚDO DA PLACA ÚNICA ---

# Abre a "Placa de Metal"
st.markdown('<div class="metal-chassis">', unsafe_allow_html=True)

# 1. NAVEGADOR SOUNDCLOUD (Lado Esquerdo da Placa)
with st.container():
    st.markdown('<div class="embedded-browser">', unsafe_allow_html=True)
    st.markdown("### ☁️ SoundCloud")
    search = st.text_input("Search World Music", placeholder="Artist, track...", label_visibility="collapsed")
    st.markdown("---")
    st.caption("BROWSE")
    st.write("🔥 Trending Charts")
    st.write("🌍 Global Top 50")
    st.write("🎧 Deep House")
    st.write("🎹 Techno Mix")
    if search:
        st.success(f"Result: {search} - Remix.mp3")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. ÁREA DE PERFORMANCE (Decks e Mixer)
with st.container():
    st.markdown('<div class="deck-area">', unsafe_allow_html=True)

    # --- DECK A (Esquerdo) ---
    with st.container():
        st.markdown('<div class="digital-display">TRACK A: READY<br>126.0 BPM</div>', unsafe_allow_html=True)
        st.markdown('<div class="jog-wheel"><div class="jog-center"></div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.button("PLAY", key="a_p")
        c2.button("CUE", key="a_c")
        st.slider("PITCH", -10.0, 10.0, 0.0, key="a_pitch")

    # --- MIXER (Centro) ---
    st.markdown('<div class="integrated-mixer">', unsafe_allow_html=True)
    st.caption("GAIN")
    st.slider("G", 0, 100, 80, key="mix_g", label_visibility="collapsed")
    st.markdown("---")
    st.caption("HIGH")
    st.slider("H", 0, 100, 50, key="mix_h", label_visibility="collapsed")
    st.caption("MID")
    st.slider("M", 0, 100, 50, key="mix_m", label_visibility="collapsed")
    st.caption("LOW")
    st.slider("L", 0, 100, 50, key="mix_l", label_visibility="collapsed")
    st.markdown("---")
    st.caption("CROSS")
    st.slider("X", -100, 100, 0, key="mix_x", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- DECK B (Direito) ---
    with st.container():
        st.markdown('<div class="digital-display" style="color:#ff2d55; border-color:#ff2d5555;">TRACK B: SYNCED<br>126.0 BPM</div>', unsafe_allow_html=True)
        st.markdown('<div class="jog-wheel" style="animation-duration: 3s;"><div class="jog-center" style="border-color:#ff2d55; box-shadow:0 0 15px #ff2d55;"></div></div>', unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        c3.button("PLAY", key="b_p")
        c4.button("CUE", key="b_c")
        st.slider("PITCH", -10.0, 10.0, 0.0, key="b_pitch")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fecha a Placa de Metal
