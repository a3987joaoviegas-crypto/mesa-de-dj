import streamlit as st

st.set_page_config(layout="wide", page_title="Hardware DJ Console")

# --- DESIGN BLINDADO (SEM CÓDIGO APARECENDO) ---
st.markdown("""
<style>
    /* Esconde absolutamente tudo o que é do sistema */
    header, footer, #MainMenu {visibility: hidden;}
    .stApp { background-color: #050505; display: flex; align-items: center; justify-content: center; }

    /* A PLACA DE METAL MACIÇA (PEÇA ÚNICA) */
    .hardware-chassis {
        background: linear-gradient(180deg, #1e1e21 0%, #0a0a0b 100%);
        width: 1000px;
        height: 480px;
        border-radius: 8px;
        border: 2px solid #252529;
        position: relative;
        box-shadow: 0 50px 100px rgba(0,0,0,1), inset 0 1px 1px rgba(255,255,255,0.05);
        display: flex;
        padding: 0;
        overflow: hidden;
    }

    /* ZONAS DA PLACA (Sem separação visual) */
    .deck {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
    }

    .mixer-center {
        width: 180px;
        background: rgba(0,0,0,0.3);
        border-left: 1px solid #1a1a1c;
        border-right: 1px solid #1a1a1c;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        padding: 20px 0;
    }

    /* O DISCO DE VINIL REALISTA */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-wheel {
        width: 300px; height: 300px;
        background: #000; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        box-shadow: inset 0 0 20px #000, 0 5px 15px rgba(0,0,0,0.5);
    }

    .vinyl-surface {
        width: 96%; height: 96%; border-radius: 50%;
        background: 
            repeating-radial-gradient(circle, #080808 0, #080808 1px, #111 2px),
            conic-gradient(from 0deg, transparent, rgba(255,255,255,0.02) 25%, transparent 50%);
        animation: spin 3s linear infinite;
        display: flex; align-items: center; justify-content: center;
    }

    .led-ring {
        width: 70px; height: 70px; background: #000;
        border: 2px solid #00f2ff; border-radius: 50%;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
    }

    /* BOTÕES EMBUTIDOS NO METAL (Pads) */
    .pad-container {
        display: flex; gap: 6px; margin-top: 20px;
    }
    .metal-pad {
        width: 45px; height: 35px; 
        background: #1a1a1c; border: 1px solid #333;
        border-radius: 3px; box-shadow: 0 2px 0 #000;
    }

    /* FADERS DO MIXER */
    .fader-track {
        width: 4px; height: 80px; background: #000; border-radius: 2px; position: relative;
    }
    .fader-cap {
        width: 24px; height: 12px; background: #333; position: absolute; left: -10px; top: 40%; border-radius: 2px;
    }
</style>
""", unsafe_allow_html=True)

# --- A ESTRUTURA FINAL (HARDWARE LIMPO) ---
st.markdown("""
<div class="hardware-chassis">
    
    <div class="deck">
        <div class="jog-wheel">
            <div class="vinyl-surface">
                <div class="led-ring"></div>
            </div>
        </div>
        <div class="pad-container">
            <div class="metal-pad" style="border-color:#00f2ff;"></div>
            <div class="metal-pad"></div>
            <div class="metal-pad"></div>
            <div class="metal-pad"></div>
        </div>
    </div>

    <div class="mixer-center">
        <div class="fader-track"><div class="fader-cap"></div></div>
        <div style="display: flex; gap: 15px;">
            <div class="fader-track" style="height: 50px;"></div>
            <div class="fader-track" style="height: 50px;"></div>
        </div>
        <div style="width: 80px; height: 4px; background: #000; position: relative; margin-top: 10px;">
            <div style="width: 10px; height: 20px; background: #333; position: absolute; left: 45%; top: -8px;"></div>
        </div>
    </div>

    <div class="deck">
        <div class="jog-wheel">
            <div class="vinyl-surface" style="animation-duration: 4s;">
                <div class="led-ring" style="border-color:#ff4b4b; box-shadow: 0 0 15px rgba(255, 75, 75, 0.4);"></div>
            </div>
        </div>
        <div class="pad-container">
            <div class="metal-pad" style="border-color:#ff4b4b;"></div>
            <div class="metal-pad"></div>
            <div class="metal-pad"></div>
            <div class="metal-pad"></div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)
