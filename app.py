import streamlit as st

# Configuração para limpar a página
st.set_page_config(layout="wide", page_title="DJ Unibody Hardware")

# CSS para esconder o "lixo" do sistema e desenhar a placa
st.markdown("""
<style>
    /* Esconde menus do Streamlit */
    header, footer, #MainMenu {visibility: hidden;}
    .stApp { background-color: #08080a; display: flex; align-items: center; justify-content: center; }

    /* O CHASSIS DE METAL (PEÇA ÚNICA) */
    .dj-console {
        background: linear-gradient(180deg, #1a1a1c 0%, #050505 100%);
        width: 1080px;
        height: 500px;
        border-radius: 12px;
        border: 2px solid #2a2a2e;
        position: relative;
        box-shadow: 0 100px 150px rgba(0,0,0,1), inset 0 1px 1px rgba(255,255,255,0.05);
        display: grid;
        grid-template-columns: 1fr 200px 1fr; /* Deck | Mixer | Deck */
        overflow: hidden;
    }

    /* Secção de Hardware */
    .section {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }

    /* O DISCO DE VINIL (FÍSICO) */
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-container {
        width: 330px; height: 330px;
        background: #000; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        box-shadow: inset 0 0 30px #000, 0 5px 15px rgba(0,0,0,0.5);
    }

    .vinyl-record {
        width: 96%; height: 96%; border-radius: 50%;
        background: 
            repeating-radial-gradient(circle, #0a0a0a 0, #0a0a0a 1px, #111 2px),
            conic-gradient(from 0deg, transparent, rgba(255,255,255,0.03) 25%, transparent 50%);
        animation: spin 4s linear infinite;
        display: flex; align-items: center; justify-content: center;
    }

    .led-center {
        width: 75px; height: 75px; background: #000;
        border: 2px solid #00f2ff; border-radius: 50%;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }

    /* MIXER CENTRAL (Embutido no metal) */
    .mixer-plate {
        background: rgba(0,0,0,0.3);
        border-left: 2px solid #1a1a1c;
        border-right: 2px solid #1a1a1c;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px 0;
        justify-content: space-around;
    }

    /* BOTÕES E FADERS (Desenhos sem código) */
    .button-pad {
        width: 50px; height: 35px; background: #1a1a1c; 
        border: 1px solid #333; border-radius: 4px;
        margin: 5px; box-shadow: 0 2px 0 #000;
    }
    
    .fader-slot {
        width: 6px; height: 100px; background: #000; 
        border-radius: 3px; position: relative;
    }
    .fader-knob {
        width: 26px; height: 14px; background: #333; 
        border: 1px solid #444; position: absolute; 
        top: 40%; left: -10px; border-radius: 2px;
    }
</style>
""", unsafe_allow_html=True)

# --- O HARDWARE FINAL (LITERALMENTE JUNTO) ---
st.markdown("""
<div class="dj-console">
    
    <div class="section">
        <div style="color: #444; font-size: 10px; margin-bottom: 10px;">DECK A</div>
        <div class="jog-container">
            <div class="vinyl-record">
                <div class="led-center"></div>
            </div>
        </div>
        <div style="display: flex; margin-top: 20px;">
            <div class="button-pad" style="border-color: #00f2ff;"></div>
            <div class="button-pad"></div>
            <div class="button-pad"></div>
            <div class="button-pad"></div>
        </div>
    </div>

    <div class="mixer-plate">
        <div style="color: #444; font-size: 10px;">MIXER</div>
        <div class="fader-slot"><div class="fader-knob"></div></div>
        <div style="display: flex; gap: 20px;">
             <div class="fader-slot" style="height: 60px;"></div>
             <div class="fader-slot" style="height: 60px;"></div>
        </div>
        <div style="width: 120px; height: 6px; background: #000; position: relative;">
            <div style="width: 14px; height: 26px; background: #333; position: absolute; left: 45%; top: -10px;"></div>
        </div>
    </div>

    <div class="section">
        <div style="color: #444; font-size: 10px; margin-bottom: 10px;">DECK B</div>
        <div class="jog-container">
            <div class="vinyl-record" style="animation-duration: 3s;">
                <div class="led-center" style="border-color: #ff4b4b; box-shadow: 0 0 20px rgba(255,75,75,0.5);"></div>
            </div>
        </div>
        <div style="display: flex; margin-top: 20px;">
            <div class="button-pad" style="border-color: #ff4b4b;"></div>
            <div class="button-pad"></div>
            <div class="button-pad"></div>
            <div class="button-pad"></div>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)
