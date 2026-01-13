import streamlit as st

st.set_page_config(layout="wide", page_title="REAL DJ HARDWARE")

# --- O CÓDIGO DA PLACA DE METAL MACIÇA ---
st.markdown("""
<style>
    /* Limpar tudo o que é "site" e deixar só o "objeto" */
    header, footer, .stSidebar {display: none;}
    .stApp { background-color: #050505; display: flex; align-items: center; justify-content: center; height: 100vh; }

    /* A PEÇA DE METAL ÚNICA (UNIBODY) */
    .dj-hardware-block {
        background: linear-gradient(180deg, #151517 0%, #080809 100%);
        width: 1100px;
        height: 520px;
        border-radius: 10px;
        border: 2px solid #222;
        box-shadow: 0 80px 150px rgba(0,0,0,1), inset 0 1px 1px rgba(255,255,255,0.05);
        display: grid;
        grid-template-columns: 1fr 220px 1fr;
        position: relative;
        padding: 20px;
        overflow: hidden;
    }

    /* Textura de Alumínio Escovado em toda a placa */
    .dj-hardware-block::before {
        content: "";
        position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 1%, transparent 2%);
        pointer-events: none;
    }

    /* DISCO DE VINIL (Encastrado no Metal) */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-hole {
        width: 330px; height: 330px;
        background: #000; border-radius: 50%;
        box-shadow: inset 0 0 20px #000, 0 2px 4px rgba(255,255,255,0.05);
        display: flex; align-items: center; justify-content: center;
        margin-top: 20px;
    }

    .vinyl-disc {
        width: 96%; height: 96%; border-radius: 50%;
        background: 
            repeating-radial-gradient(circle, #080808 0, #080808 1px, #111 2px),
            conic-gradient(from 0deg, transparent, rgba(255,255,255,0.03) 25%, transparent 50%);
        animation: spin 3s linear infinite;
        display: flex; align-items: center; justify-content: center;
    }

    /* BOTÕES QUADRADOS DE PERFORMANCE (Logo abaixo do disco) */
    .pad-container {
        display: grid; grid-template-columns: repeat(4, 1fr);
        gap: 8px; width: 300px; margin-top: 15px;
    }

    .dj-pad {
        height: 40px; background: #1a1a1c; border: 1px solid #333;
        border-radius: 4px; box-shadow: 0 2px 0 #000;
    }

    /* MIXER CENTRAL (Parte da mesma chapa) */
    .mixer-center {
        background: rgba(0,0,0,0.3);
        border-left: 1px solid #1a1a1c; border-right: 1px solid #1a1a1c;
        display: flex; flex-direction: column; align-items: center;
        padding: 10px; justify-content: space-around;
    }

    /* Ecrã de Informação embutido no centro superior */
    .central-lcd {
        position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
        width: 180px; height: 100px; background: #000;
        border: 1px solid #222; border-radius: 4px;
        color: #00f2ff; font-family: monospace; font-size: 11px;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        box-shadow: inset 0 0 10px rgba(0,242,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- ESTRUTURA FÍSICA ---

st.markdown(f"""
<div class="dj-hardware-block">
    <div class="central-lcd">
        <div>MASTER OUT</div>
        <div style="font-size: 18px; margin: 5px 0;">128.0</div>
        <div style="color: #444;">BPM SYNC</div>
    </div>

    <div style="display: flex; flex-direction: column; align-items: center;">
        <div class="jog-hole">
            <div class="vinyl-disc">
                <div style="width: 70px; height: 70px; background: #000; border: 2px solid #00f2ff; border-radius: 50%; box-shadow: 0 0 15px #00f2ff55;"></div>
            </div>
        </div>
        <div class="pad-container">
            <div class="dj-pad"></div><div class="dj-pad"></div>
            <div class="dj-pad"></div><div class="dj-pad"></div>
        </div>
    </div>

    <div class="mixer-center">
        <div style="margin-top: 100px; width: 100%;">
            </div>
    </div>

    <div style="display: flex; flex-direction: column; align-items: center;">
        <div class="jog-hole">
            <div class="vinyl-disc" style="animation-duration: 4s;">
                <div style="width: 70px; height: 70px; background: #000; border: 2px solid #ff4b4b; border-radius: 50%; box-shadow: 0 0 15px #ff4b4b55;"></div>
            </div>
        </div>
        <div class="pad-container">
            <div class="dj-pad"></div><div class="dj-pad"></div>
            <div class="dj-pad"></div><div class="dj-pad"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Injetar os controlos Python no "buraco" do Mixer
with st.sidebar: # Usamos a sidebar apenas para organizar os inputs, mas eles podiam estar invisíveis
    st.write("Controlos Internos")

# Para que os sliders apareçam "dentro" do mixer na placa:
st.markdown('<style>.stSlider {margin-top: -30px !important;}</style>', unsafe_allow_html=True)
