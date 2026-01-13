import streamlit as st

st.set_page_config(layout="wide", page_title="Hardware DJ Unibody")

# --- O DESIGN DO HARDWARE MACIÇO (TUDO JUNTO) ---
st.markdown("""
<style>
    .stApp { background-color: #050505; }

    /* A PLACA DE METAL MACIÇA (CHASSIS ÚNICO) */
    .dj-hardware-body {
        background: linear-gradient(180deg, #1a1a1c 0%, #0a0a0b 100%);
        width: 1000px;
        height: 480px;
        margin: 50px auto;
        border-radius: 8px;
        border: 2px solid #2a2a2e;
        position: relative; /* Para permitir posicionar botões colados ao disco */
        box-shadow: 0 40px 80px rgba(0,0,0,0.9), inset 0 1px 1px rgba(255,255,255,0.1);
        display: grid;
        grid-template-columns: 1fr 200px 1fr;
        overflow: hidden;
    }

    /* Textura de metal escovado para a placa toda */
    .dj-hardware-body::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 1%, transparent 2%);
        pointer-events: none;
    }

    /* DECK SECTION (Ocupa o lado sem divisões) */
    .deck-section {
        position: relative;
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* O DISCO DE VINIL (Tamanho grande e centralizado no deck) */
    @keyframes spin_vinyl { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-wheel {
        width: 290px;
        height: 290px;
        border-radius: 50%;
        background: radial-gradient(circle, #222 10%, #000 100%);
        border: 10px solid #161618;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5), inset 0 0 15px #000;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: spin_vinyl 4s linear infinite;
        position: relative;
    }

    .vinyl-grooves {
        width: 96%; height: 96%; border-radius: 50%;
        background: repeating-radial-gradient(circle, #000 0, #000 1px, #0a0a0a 2px);
        display: flex; align-items: center; justify-content: center;
    }

    .jog-center {
        width: 65px; height: 65px; background: #000;
        border: 2px solid #00f2ff; border-radius: 50%;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
    }

    /* PAINEL DE BOTÕES (Colados à volta do disco) */
    .button-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
        width: 280px;
        margin-top: 15px;
    }

    /* MIXER SECTION (Centralizado na mesma placa) */
    .mixer-section {
        background: rgba(0,0,0,0.4);
        border-left: 1px solid #222;
        border-right: 1px solid #222;
        padding: 15px 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
    }

    /* Estilo dos Knobs e Faders */
    .stSlider { margin-bottom: -15px !important; }
    .stSlider label { color: #555 !important; font-size: 10px !important; }

    /* Estética de Hardware dos Botões */
    .stButton>button {
        width: 100% !important;
        background: #1c1c1e !important;
        border: 1px solid #333 !important;
        color: #888 !important;
        font-size: 10px !important;
        height: 35px !important;
        border-radius: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- MONTAGEM DA CONTROLADORA ---

st.markdown('<div class="dj-hardware-body">', unsafe_allow_html=True)

# 1. DECK ESQUERDO
with st.container():
    st.markdown('<div class="deck-section">', unsafe_allow_html=True)
    # Ecrã LCD do Deck
    st.markdown('<div style="background:#000; color:#00f2ff; padding:5px; width:120px; text-align:center; font-family:monospace; font-size:10px; border:1px solid #333; margin-bottom:10px;">128.00 BPM</div>', unsafe_allow_html=True)
    # Jog Wheel
    st.markdown('<div class="jog-wheel"><div class="vinyl-grooves"><div class="jog-center"></div></div></div>', unsafe_allow_html=True)
    # Botões colados por baixo
    st.markdown('<div class="button-grid">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.button("PLAY", key="p1")
    c2.button("CUE", key="c1")
    c3.button("SYNC", key="s1")
    c4.button("SHIFT", key="sh1")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. MIXER CENTRAL (Embutido)
with st.container():
    st.markdown('<div class="mixer-section">', unsafe_allow_html=True)
    st.slider("GAIN", 0, 100, 70, key="m_g")
    st.slider("HI", 0, 100, 50, key="m_h")
    st.slider("MID", 0, 100, 50, key="m_m")
    st.slider("LOW", 0, 100, 50, key="m_l")
    st.markdown("<br>", unsafe_allow_html=True)
    st.slider("CROSSFADER", -100, 100, 0, key="m_x")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. DECK DIREITO
with st.container():
    st.markdown('<div class="deck-section">', unsafe_allow_html=True)
    # Ecrã LCD do Deck B
    st.markdown('<div style="background:#000; color:#ff4b4b; padding:5px; width:120px; text-align:center; font-family:monospace; font-size:10px; border:1px solid #333; margin-bottom:10px;">128.00 BPM</div>', unsafe_allow_html=True)
    # Jog Wheel
    st.markdown('<div class="jog-wheel"><div class="vinyl-grooves"><div class="jog-center" style="border-color:#ff4b4b; box-shadow:0 0 15px #ff4b4b66;"></div></div></div>', unsafe_allow_html=True)
    # Botões colados por baixo
    st.markdown('<div class="button-grid">', unsafe_allow_html=True)
    c5, c6, c7, c8 = st.columns(4)
    c5.button("PLAY", key="p2")
    c6.button("CUE", key="c2")
    c7.button("SYNC", key="s2")
    c8.button("SHIFT", key="sh2")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
