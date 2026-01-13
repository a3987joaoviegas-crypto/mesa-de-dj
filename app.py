import streamlit as st

# Configuração de layout limpo
st.set_page_config(layout="wide", page_title="Gemini Ultra-Realistic DJ Console")

# --- CSS DE ENGENHARIA VISUAL (HARDWARE PURO) ---
st.markdown("""
<style>
    /* Fundo do Estúdio */
    .stApp {
        background: radial-gradient(circle at center, #1b1b1e 0%, #050505 100%);
    }

    /* CHASSIS DE METAL INTEGRADO */
    .dj-system-unibody {
        background: linear-gradient(145deg, #232326 0%, #131315 100%);
        border: 2px solid #323236;
        border-radius: 30px;
        box-shadow: 
            0 50px 100px rgba(0,0,0,0.9),
            inset 0 1px 3px rgba(255,255,255,0.1);
        padding: 40px;
        margin: 20px auto;
        width: 95%;
        display: flex;
        flex-direction: column;
        gap: 30px;
        position: relative;
    }

    /* Brilho de Metal Escovado */
    .dj-system-unibody::after {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 1%, transparent 2%);
        pointer-events: none;
        border-radius: 30px;
    }

    /* SEÇÃO SUPERIOR (Displays e Navegação) */
    .top-panel {
        display: grid;
        grid-template-columns: 280px 1fr 280px;
        gap: 20px;
        height: 250px;
    }

    /* Ecrãs LCD Realistas */
    .lcd-screen {
        background: #000;
        border: 3px solid #2a2a2e;
        border-radius: 10px;
        padding: 15px;
        box-shadow: inset 0 0 20px rgba(0, 242, 255, 0.15);
        color: #00f2ff;
        font-family: 'Courier New', monospace;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-shadow: 0 0 5px #00f2ff;
    }

    /* SEÇÃO DE PERFORMANCE (Discos e Mixer) */
    .performance-deck {
        display: grid;
        grid-template-columns: 1fr 220px 1fr;
        gap: 30px;
        align-items: center;
    }

    /* JOG WHEEL (O Disco que Gira) */
    @keyframes spin_deck { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .jog-outer {
        width: 340px;
        height: 340px;
        border-radius: 50%;
        background: #0a0a0b;
        border: 10px solid #252528;
        box-shadow: 0 15px 40px rgba(0,0,0,0.8), inset 0 0 20px #000;
        margin: auto;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }

    .jog-inner-vinyl {
        width: 90%;
        height: 90%;
        border-radius: 50%;
        background: repeating-radial-gradient(circle, #111 0, #111 2px, #161618 3px);
        animation: spin_deck 4s linear infinite;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .jog-center-display {
        width: 80px;
        height: 80px;
        background: #000;
        border: 2px solid #00f2ff;
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.5);
        z-index: 10;
    }

    /* MIXER VERTICAL */
    .mixer-strip {
        background: rgba(0,0,0,0.4);
        border: 2px solid #2a2a2e;
        border-radius: 15px;
        height: 450px;
        padding: 20px 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        box-shadow: inset 0 0 15px #000;
    }

    /* Botões LED (Play/Cue) */
    .dj-btn {
        padding: 15px !important;
        font-weight: bold !important;
        border-radius: 50% !important; /* Botões redondos na imagem */
        width: 70px !important;
        height: 70px !important;
        border: 2px solid #3a3a3e !important;
        background: #1e1e21 !important;
        transition: 0.2s !important;
    }
    
    .stButton>button:hover {
        border-color: #00f2ff !important;
        color: #00f2ff !important;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4) !important;
    }

    /* Esconder labels dos sliders para assemelhar a faders */
    .stSlider label { display: none; }
</style>
""", unsafe_allow_html=True)

# --- ESTRUTURA DA APP ---

st.markdown('<div class="dj-system-unibody">', unsafe_allow_html=True)

# 1. PAINEL SUPERIOR (Displays e Navegação)
col_nav_L, col_center_display, col_nav_R = st.columns([1, 2, 1])

with col_nav_L:
    st.markdown("""<div class="lcd-screen" style="height: 100px;">
        <small>BROWSER</small><br><b>SOUNDCLOUD ACTIVE</b>
    </div>""", unsafe_allow_html=True)

with col_center_display:
    st.markdown("""<div class="lcd-screen" style="height: 100px; border-color: #ff4b4b33; color: #ff4b4b;">
        <h2>GEMINI DIGITAL DJ DECK</h2>
        <small>MASTER OUTPUT: -3.2dB | BPM: 128.0</small>
    </div>""", unsafe_allow_html=True)

with col_nav_R:
    st.markdown("""<div class="lcd-screen" style="height: 100px;">
        <small>EFFECTS</small><br><b>REVERB: OFF</b>
    </div>""", unsafe_allow_html=True)

# 2. ÁREA DE PERFORMANCE PRINCIPAL
st.markdown('<div class="performance-deck">', unsafe_allow_html=True)

# --- DECK A (ESQUERDO) ---
with st.container():
    st.markdown('<div class="jog-outer"><div class="jog-inner-vinyl"><div class="jog-center-display"></div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.button("▶️", key="play_a")
    c2.button("⏸️", key="cue_a")
    c3.button("🔄", key="sync_a")
    st.markdown("<br>", unsafe_allow_html=True)
    st.slider("Tempo A", -10.0, 10.0, 0.0, key="sl_a")

# --- MIXER CENTRAL ---
st.markdown('<div class="mixer-strip">', unsafe_allow_html=True)
st.caption("GAIN")
st.slider("G", 0, 100, 75, key="m_g")
st.markdown("---")
st.caption("HIGH")
st.slider("H", 0, 100, 50, key="m_h")
st.caption("MID")
st.slider("M", 0, 100, 50, key="m_m")
st.caption("LOW")
st.slider("L", 0, 100, 50, key="m_l")
st.markdown("---")
st.caption("FADER")
st.slider("F", 0, 100, 80, key="m_f")
st.markdown('</div>', unsafe_allow_html=True)

# --- DECK B (DIREITO) ---
with st.container():
    st.markdown('<div class="jog-outer"><div class="jog-inner-vinyl" style="animation-duration: 4.5s;"><div class="jog-center-display" style="border-color: #ff4b4b; box-shadow: 0 0 15px #ff4b4b;"></div></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    c4.button("▶️", key="play_b")
    c5.button("⏸️", key="cue_b")
    c6.button("🔄", key="sync_b")
    st.markdown("<br>", unsafe_allow_html=True)
    st.slider("Tempo B", -10.0, 10.0, 0.0, key="sl_b")

st.markdown('</div>', unsafe_allow_html=True) # Fim da Performance Deck

# 3. NAVEGADOR SOUNDCLOUD (Embutido no fundo da placa)
st.markdown("---")
st.markdown("### 🔍 SoundCloud Integrated Library")
st.text_input("Search tracks worldwide...", placeholder="Type artist or song name...")
st.markdown("""
<div style="display: flex; gap: 10px; overflow-x: auto; padding: 10px;">
    <div style="min-width: 200px; background: #000; padding: 10px; border-radius: 5px; border-left: 3px solid #00f2ff;">🎵 Tech House 2024</div>
    <div style="min-width: 200px; background: #000; padding: 10px; border-radius: 5px; border-left: 3px solid #ff4b4b;">🎵 Techno Bunker</div>
    <div style="min-width: 200px; background: #000; padding: 10px; border-radius: 5px; border-left: 3px solid #00f2ff;">🎵 Deep Vibes</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Fim do Unibody Chassis
