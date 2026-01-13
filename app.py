import streamlit as st

st.set_page_config(layout="wide", page_title="Hardware DJ Console")

# --- O DESIGN DO HARDWARE MACIÇO (TUDO JUNTO) ---
st.markdown("""
<style>
    /* Esconde elementos padrão do Streamlit para focar na placa */
    header, footer {visibility: hidden;}
    .stApp { background-color: #0d0d0f; }

    /* A PLACA DE METAL MACIÇA (CHASSIS ÚNICO) */
    .dj-hardware-unit {
        background: linear-gradient(180deg, #1e1e21 0%, #0a0a0b 100%);
        width: 1100px;
        height: 550px;
        margin: 20px auto;
        border-radius: 12px;
        border: 3px solid #2a2a2e;
        position: relative;
        box-shadow: 0 60px 120px rgba(0,0,0,1), inset 0 1px 2px rgba(255,255,255,0.05);
        display: flex;
        padding: 0;
        overflow: hidden;
    }

    /* Textura de Metal Escovado */
    .dj-hardware-unit::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 1%, transparent 2%);
        pointer-events: none;
        z-index: 1;
    }

    /* Ecrã Central (Como na Numark) */
    .master-screen {
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 320px;
        height: 180px;
        background: #000;
        border: 2px solid #333;
        border-radius: 4px;
        z-index: 2;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: #00f2ff;
        font-family: monospace;
        box-shadow: inset 0 0 20px rgba(0, 242, 255, 0.1);
    }

    /* Jog Wheels (Discos) */
    @keyframes rotate_disc { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-wheel {
        width: 340px;
        height: 340px;
        background: radial-gradient(circle, #222 5%, #050505 100%);
        border-radius: 50%;
        border: 10px solid #1a1a1c;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: rotate_disc 4s linear infinite;
        box-shadow: 0 15px 30px rgba(0,0,0,0.8), inset 0 0 10px #000;
        z-index: 2;
    }

    .vinyl-texture {
        width: 98%; height: 98%; border-radius: 50%;
        background: repeating-radial-gradient(circle, #000 0, #000 1px, #111 2px);
        display: flex; align-items: center; justify-content: center;
    }

    .led-center {
        width: 75px; height: 75px; background: #000;
        border: 3px solid #00f2ff; border-radius: 50%;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }

    /* Mixer Central (Integrado na placa) */
    .mixer-strip {
        width: 200px;
        height: 100%;
        background: rgba(0,0,0,0.2);
        border-left: 1px solid #222;
        border-right: 1px solid #222;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 210px; /* Espaço para o ecrã */
        z-index: 2;
    }

    /* Botões de Performance (Abaixo do disco) */
    .pad-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 6px;
        width: 280px;
        margin-top: 20px;
        z-index: 2;
    }
</style>
""", unsafe_allow_html=True)

# --- ESTRUTURA DA PLACA ÚNICA ---

# Abre o Bloco Maciço
st.markdown('<div class="dj-hardware-unit">', unsafe_allow_html=True)

# ECRÃ CENTRAL EMBUTIDO
st.markdown("""
<div class="master-screen">
    <div style="font-size: 10px; color: #555;">SOUNDCLOUD CONNECTED</div>
    <div style="font-size: 20px;">GEMINI PRO</div>
    <div style="margin-top: 10px; color: #ff4b4b;">128.00 BPM</div>
    <div style="width: 80%; height: 40px; border-bottom: 1px solid #222; margin-top: 5px;"></div>
</div>
""", unsafe_allow_html=True)

# LADO ESQUERDO (DECK A)
with st.container():
    st.markdown('<div style="flex:1; display:flex; flex-direction:column; align-items:center; padding-top:40px; z-index:2;">', unsafe_allow_html=True)
    st.markdown('<div class="jog-wheel"><div class="vinyl-texture"><div class="led-center"></div></div></div>', unsafe_allow_html=True)
    
    # Pads/Botões integrados
    st.markdown('<div class="pad-grid">', unsafe_allow_html=True)
    cols = st.columns(4)
    for i in range(4):
        cols[i].button("PLAY" if i==0 else "CUE", key=f"btn_a_{i}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# CENTRO (MIXER)
with st.container():
    st.markdown('<div class="mixer-strip">', unsafe_allow_html=True)
    st.slider("GAIN", 0, 100, 75, key="gain", label_visibility="collapsed")
    st.slider("HI", 0, 100, 50, key="hi", label_visibility="collapsed")
    st.slider("MID", 0, 100, 50, key="mid", label_visibility="collapsed")
    st.slider("LOW", 0, 100, 50, key="low", label_visibility="collapsed")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.slider("FADER", -100, 100, 0, key="xfade", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# LADO DIREITO (DECK B)
with st.container():
    st.markdown('<div style="flex:1; display:flex; flex-direction:column; align-items:center; padding-top:40px; z-index:2;">', unsafe_allow_html=True)
    st.markdown('<div class="jog-wheel"><div class="vinyl-texture"><div class="led-center" style="border-color:#ff4b4b; box-shadow:0 0 20px #ff4b4b88;"></div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="pad-grid">', unsafe_allow_html=True)
    cols_b = st.columns(4)
    for i in range(4):
        cols_b[i].button("PLAY" if i==0 else "CUE", key=f"btn_b_{i}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fecha o Bloco Maciço

st.caption("Controlo Unibody Ativo: Todos os componentes estão montados na mesma chapa de metal.")
