import streamlit as st

# Configuração de ecrã inteiro para simular a consola
st.set_page_config(layout="wide", page_title="Hardware DJ Console")

# --- CSS DE ENGENHARIA INDUSTRIAL (O DESIGN DA PLACA REAL) ---
st.markdown("""
<style>
    .stApp { background-color: #050505; }

    /* A PLACA DE METAL ÚNICA (O CHASSIS) */
    .dj-chassis {
        background: linear-gradient(145deg, #1e1e21 0%, #0d0d0f 100%);
        border: 2px solid #2d2d30;
        border-radius: 20px;
        padding: 30px;
        margin: 20px auto;
        width: 95%;
        display: grid;
        grid-template-columns: 1fr 180px 1fr; /* Deck | Mixer | Deck */
        gap: 0px; /* Sem espaços entre as secções, tudo na mesma chapa */
        box-shadow: 
            0 50px 100px rgba(0,0,0,0.9),
            inset 0 1px 2px rgba(255,255,255,0.05);
        position: relative;
    }

    /* Secção de Metal (Efeito de ranhuras no hardware) */
    .metal-section {
        border-right: 1px solid #222;
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* O DISCO DE VINIL REALISTA */
    @keyframes spin_vinyl { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    .jog-hole {
        width: 340px;
        height: 340px;
        background: #000;
        border-radius: 50%;
        padding: 10px;
        box-shadow: inset 0 0 20px #000, 0 2px 5px rgba(255,255,255,0.05);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .vinyl-record {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: 
            repeating-radial-gradient(circle, #080808 0%, #080808 0.05%, #111 0.1%),
            conic-gradient(from 0deg, transparent 0%, rgba(255,255,255,0.03) 25%, transparent 50%, rgba(255,255,255,0.03) 75%, transparent 100%);
        animation: spin_vinyl 4s linear infinite;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Detalhes do Centro do Disco */
    .vinyl-center {
        width: 70px;
        height: 70px;
        background: #000;
        border: 2px solid #00f2ff;
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
    }

    /* Faders e Sliders estilo Mesa de Mistura */
    .stSlider label { color: #555 !important; font-size: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# --- CONTEÚDO INSERIDO NA PLACA ---

st.markdown('<div class="dj-chassis">', unsafe_allow_html=True)

# 1. DECK ESQUERDO (Inserido na Placa)
with st.container():
    st.markdown('<div class="metal-section">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#555; margin-bottom:20px;'>DECK A</h4>", unsafe_allow_html=True)
    st.markdown('<div class="jog-hole"><div class="vinyl-record"><div class="vinyl-center"></div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.button("PLAY", key="a1")
    col2.button("CUE", key="a2")
    st.slider("PITCH CONTROL", -10.0, 10.0, 0.0, key="s1")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. MIXER CENTRAL (Inserido na Placa)
with st.container():
    st.markdown('<div class="metal-section" style="background: rgba(0,0,0,0.2);">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#555;'>MIXER</h4>", unsafe_allow_html=True)
    st.slider("HI", 0, 100, 50, key="m1")
    st.slider("MID", 0, 100, 50, key="m2")
    st.slider("LOW", 0, 100, 50, key="m3")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.slider("CROSSFADER", -100, 100, 0, key="m4")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. DECK DIREITO (Inserido na Placa)
with st.container():
    st.markdown('<div class="metal-section" style="border-right:none;">', unsafe_allow_html=True)
    st.markdown("<h4 style='color:#555; margin-bottom:20px;'>DECK B</h4>", unsafe_allow_html=True)
    st.markdown('<div class="jog-hole"><div class="vinyl-record" style="animation-duration: 3s;"><div class="vinyl-center" style="border-color:#ff2d55; box-shadow: 0 0 15px rgba(255,45,85,0.4);"></div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    col3.button("PLAY", key="b1")
    col4.button("CUE", key="b2")
    st.slider("PITCH CONTROL", -10.0, 10.0, 0.0, key="s2")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
