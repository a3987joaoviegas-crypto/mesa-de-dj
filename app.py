import streamlit as st

st.set_page_config(layout="wide", page_title="Gemini Ultra-Realistic Console")

# --- CSS DE ALTA PRECISÃO (HARDWARE PURO) ---
st.markdown("""
<style>
    /* Esconde elementos desnecessários */
    header, footer {visibility: hidden;}
    .stApp { background-color: #0b0b0d; display: flex; align-items: center; justify-content: center; }

    /* A PLACA ÚNICA (O CHASSIS DE METAL) */
    .dj-unibody {
        background: linear-gradient(145deg, #1e1e21, #080809);
        width: 1050px;
        height: 500px;
        border: 3px solid #2a2a2e;
        border-radius: 15px;
        position: relative;
        box-shadow: 0 50px 100px rgba(0,0,0,1), inset 0 1px 2px rgba(255,255,255,0.05);
        display: flex;
        justify-content: space-between;
        padding: 40px;
        overflow: hidden;
    }

    /* Textura de Metal Escovado Integrada */
    .dj-unibody::after {
        content: "";
        position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 1%, transparent 2%);
        pointer-events: none;
    }

    /* O DISCO DE VINIL (Encastrado) */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-hole {
        width: 320px; height: 320px;
        background: #000; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        box-shadow: inset 0 0 25px #000;
        position: relative;
    }

    .vinyl-plate {
        width: 95%; height: 95%; border-radius: 50%;
        background: 
            repeating-radial-gradient(circle, #0a0a0a 0, #0a0a0a 1px, #111 2px),
            conic-gradient(from 0deg, transparent, rgba(255,255,255,0.03) 25%, transparent 50%);
        animation: spin 4s linear infinite;
        display: flex; align-items: center; justify-content: center;
    }

    .led-center {
        width: 70px; height: 70px; background: #000;
        border: 2px solid #00f2ff; border-radius: 50%;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }

    /* MIXER CENTRAL (Sem texto, apenas os faders) */
    .mixer-core {
        width: 180px;
        height: 100%;
        background: rgba(0,0,0,0.2);
        border-left: 1px solid #222;
        border-right: 1px solid #222;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }

    /* Simuladores de Botões e Sliders na Placa */
    .fake-fader {
        width: 4px; height: 120px; background: #111; border-radius: 2px; position: relative;
    }
    .fake-fader::after {
        content: ""; position: absolute; top: 30%; left: -10px;
        width: 24px; height: 12px; background: #333; border: 1px solid #444; border-radius: 2px;
    }

    .pad-row {
        display: flex; gap: 8px; margin-top: 20px;
    }
    .hw-pad {
        width: 50px; height: 35px; background: #1a1a1c; border: 1px solid #333; border-radius: 3px;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- CONSTRUÇÃO VISUAL ---

st.markdown("""
<div class="dj-unibody">
    
    <div style="display: flex; flex-direction: column; align-items: center;">
        <div class="jog-hole">
            <div class="vinyl-plate">
                <div class="led-center"></div>
            </div>
        </div>
        <div class="pad-row">
            <div class="hw-pad" style="border-color: #00f2ff; box-shadow: 0 0 10px rgba(0,242,255,0.2);"></div>
            <div class="hw-pad"></div>
            <div class="hw-pad"></div>
            <div class="hw-pad"></div>
        </div>
    </div>

    <div class="mixer-core">
        <div style="color: #444; font-size: 10px; font-family: sans-serif;">MASTER LEVEL</div>
        <div class="fake-fader"></div>
        <div style="display: flex; gap: 15px;">
            <div class="fake-fader" style="height: 80px;"></div>
            <div class="fake-fader" style="height: 80px;"></div>
        </div>
        <div style="width: 100px; height: 4px; background: #111; border-radius: 2px; position: relative; margin-top: 20px;">
            <div style="position: absolute; left: 45%; top: -10px; width: 12px; height: 24px; background: #333; border: 1px solid #444;"></div>
        </div>
    </div>

    <div style="display: flex; flex-direction: column; align-items: center;">
        <div class="jog-hole">
            <div class="vinyl-plate" style="animation-duration: 3s;">
                <div class="led-center" style="border-color: #ff4b4b; box-shadow: 0 0 20px rgba(255,75,75,0.5);"></div>
            </div>
        </div>
        <div class="pad-row">
            <div class="hw-pad" style="border-color: #ff4b4b; box-shadow: 0 0 10px rgba(255,75,75,0.2);"></div>
            <div class="hw-pad"></div>
            <div class="hw-pad"></div>
            <div class="hw-pad"></div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#333; font-family:sans-serif;'>HARDWARE UNIBODY - SEM INTERFERÊNCIA DE CÓDIGO EXTERNO</p>", unsafe_allow_html=True)
