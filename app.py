import streamlit as st

st.set_page_config(layout="wide", page_title="Hardware DJ Console")

# --- CSS DE MONTAGEM INDUSTRIAL (TUDO NUMA CHAPA SÓ) ---
st.markdown("""
<style>
    .stApp { background-color: #0e0e10; }

    /* A CONSOLA ÚNICA (SEM ESPAÇOS) */
    .dj-console-body {
        background: linear-gradient(180deg, #1a1a1c 0%, #0a0a0b 100%);
        width: 1100px;
        height: 520px;
        margin: 40px auto;
        border-radius: 10px;
        border: 4px solid #2a2a2e;
        box-shadow: 0 60px 100px rgba(0,0,0,0.9), inset 0 1px 1px rgba(255,255,255,0.1);
        
        /* O segredo: Um grid que junta Deck A | Mixer | Deck B sem folgas */
        display: grid;
        grid-template-columns: 1fr 220px 1fr;
        padding: 0;
        overflow: hidden;
    }

    /* Zonas da Placa */
    .deck-plate {
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        position: relative;
    }

    .mixer-plate {
        background: rgba(0,0,0,0.3);
        border-left: 2px solid #222;
        border-right: 2px solid #222;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px 0;
        justify-content: space-around;
    }

    /* O DISCO DE VINIL (Encostado aos botões) */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-wheel {
        width: 320px;
        height: 320px;
        border-radius: 50%;
        background: radial-gradient(circle, #111 10%, #050505 100%);
        border: 8px solid #1a1a1c;
        box-shadow: inset 0 0 15px #000, 0 5px 15px rgba(0,0,0,0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        animation: spin 4s linear infinite;
        margin-bottom: 20px;
    }

    .vinyl-texture {
        width: 98%; height: 98%; border-radius: 50%;
        background: repeating-radial-gradient(circle, #000 0, #000 1px, #0f0f0f 2px);
        display: flex; align-items: center; justify-content: center;
    }

    .center-display {
        width: 80px; height: 80px; background: #000;
        border: 2px solid #00f2ff; border-radius: 50%;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
    }

    /* BOTÕES E FADERS (Justapostos na placa) */
    .button-row {
        display: flex;
        gap: 10px;
        width: 100%;
        justify-content: center;
    }

    .hw-button {
        width: 50px; height: 50px;
        background: #222;
        border: 1px solid #333;
        border-radius: 4px;
        box-shadow: 0 2px 0 #111;
    }

    /* Estilo dos Sliders do Mixer */
    .stSlider { padding: 0px 20px; }
</style>
""", unsafe_allow_html=True)

# --- CONSTRUÇÃO DO HARDWARE ---

st.markdown('<div class="dj-console-body">', unsafe_allow_html=True)

# 1. DECK ESQUERDO (Aparafusado na placa)
with st.container():
    st.markdown('<div class="deck-plate">', unsafe_allow_html=True)
    st.markdown('<div style="color:#444; font-size:12px; font-weight:bold;">DECK A</div>', unsafe_allow_html=True)
    st.markdown('<div class="jog-wheel"><div class="vinyl-texture"><div class="center-display"></div></div></div>', unsafe_allow_html=True)
    
    # Botões logo por baixo do disco (sem espaço)
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.button("PLAY", key="a1")
    c2.button("CUE", key="a2")
    c3.button("LOOP", key="a3")
    c4.button("SYNC", key="a4")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. MIXER (O coração da placa)
with st.container():
    st.markdown('<div class="mixer-plate">', unsafe_allow_html=True)
    st.write("LEVEL")
    st.slider("GAIN", 0, 100, 80, key="m_g", label_visibility="collapsed")
    st.write("EQ")
    st.slider("HI", 0, 100, 50, key="m_h", label_visibility="collapsed")
    st.slider("MID", 0, 100, 50, key="m_m", label_visibility="collapsed")
    st.slider("LOW", 0, 100, 50, key="m_l", label_visibility="collapsed")
    st.write("CROSSFADER")
    st.slider("X", -100, 100, 0, key="m_x", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. DECK DIREITO (Justaposto ao mixer)
with st.container():
    st.markdown('<div class="deck-plate">', unsafe_allow_html=True)
    st.markdown('<div style="color:#444; font-size:12px; font-weight:bold;">DECK B</div>', unsafe_allow_html=True)
    st.markdown('<div class="jog-wheel"><div class="vinyl-texture"><div class="center-display" style="border-color:#ff2d55; box-shadow: 0 0 20px rgba(255, 45, 85, 0.4);"></div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    c5, c6, c7, c8 = st.columns(4)
    c5.button("PLAY", key="b1")
    c6.button("CUE", key="b2")
    c7.button("LOOP", key="b3")
    c8.button("SYNC", key="b4")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#333;'>Pressione Play para ativar a rotação física</p>", unsafe_allow_html=True)
