import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Gemini Hardware")

# Design da Placa em HTML/CSS Puro (Isolado do Streamlit)
hardware_html = """
<style>
    body { background-color: #050505; margin: 0; display: flex; align-items: center; justify-content: center; height: 100vh; font-family: sans-serif; overflow: hidden; }
    
    /* A PLACA DE METAL MACIÇA (UNIBODY) */
    .chassis {
        background: linear-gradient(180deg, #1e1e21 0%, #0a0a0b 100%);
        width: 1000px;
        height: 480px;
        border-radius: 12px;
        border: 2px solid #2a2a2e;
        position: relative;
        box-shadow: 0 60px 120px rgba(0,0,0,1), inset 0 1px 1px rgba(255,255,255,0.05);
        display: flex;
        padding: 0;
    }

    /* Textura de Metal Escovado Unificada */
    .chassis::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.01) 1%, transparent 2%);
        pointer-events: none; opacity: 0.5;
    }

    /* ZONAS DA PLACA (SEM DIVISÕES) */
    .deck { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 2; }
    .mixer { width: 180px; background: rgba(0,0,0,0.3); border-left: 1px solid #1a1a1c; border-right: 1px solid #1a1a1c; display: flex; flex-direction: column; align-items: center; justify-content: space-around; padding: 40px 0; z-index: 2; }

    /* O DISCO DE VINIL (DEEP BLACK) */
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .jog-wheel {
        width: 310px; height: 310px; background: #000; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        box-shadow: inset 0 0 30px #000, 0 10px 20px rgba(0,0,0,0.6);
    }
    .vinyl {
        width: 96%; height: 96%; border-radius: 50%;
        background: repeating-radial-gradient(circle, #080808 0, #080808 1px, #111 2px);
        animation: rotate 4s linear infinite;
        display: flex; align-items: center; justify-content: center;
    }
    .center-led { width: 70px; height: 70px; background: #000; border-radius: 50%; border: 2px solid #00f2ff; box-shadow: 0 0 20px rgba(0,242,255,0.4); }

    /* COMPONENTES DE HARDWARE (BOTÕES E FADERS) */
    .pads { display: flex; gap: 8px; margin-top: 25px; }
    .pad { width: 45px; height: 35px; background: #1a1a1c; border: 1px solid #333; border-radius: 3px; box-shadow: 0 2px 0 #000; }
    .fader-track { width: 6px; height: 100px; background: #000; border-radius: 3px; position: relative; }
    .fader-knob { width: 24px; height: 12px; background: #333; position: absolute; left: -9px; top: 40%; border-radius: 2px; border: 1px solid #444; }
    
    .label { color: #444; font-size: 10px; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px; }
</style>

<div class="chassis">
    <div class="deck">
        <div class="label">GEMINI DECK A</div>
        <div class="jog-wheel">
            <div class="vinyl"><div class="center-led"></div></div>
        </div>
        <div class="pads">
            <div class="pad" style="border-color: #00f2ff;"></div>
            <div class="pad"></div><div class="pad"></div><div class="pad"></div>
        </div>
    </div>

    <div class="mixer">
        <div class="label">MIXER</div>
        <div class="fader-track"><div class="fader-knob"></div></div>
        <div style="display:flex; gap: 15px;">
            <div class="fader-track" style="height: 60px;"></div>
            <div class="fader-track" style="height: 60px;"></div>
        </div>
        <div style="width: 100px; height: 6px; background: #000; position: relative;">
            <div style="width: 12px; height: 24px; background: #222; position: absolute; left: 45%; top: -9px; border: 1px solid #333;"></div>
        </div>
    </div>

    <div class="deck">
        <div class="label">GEMINI DECK B</div>
        <div class="jog-wheel">
            <div class="vinyl" style="animation-duration: 3s;"><div class="center-led" style="border-color: #ff4b4b; box-shadow: 0 0 20px rgba(255,75,75,0.4);"></div></div>
        </div>
        <div class="pads">
            <div class="pad" style="border-color: #ff4b4b;"></div>
            <div class="pad"></div><div class="pad"></div><div class="pad"></div>
        </div>
    </div>
</div>
"""

# Renderiza o componente isolado (sem interferência do Streamlit)
components.html(hardware_html, height=600)
